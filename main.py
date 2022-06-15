from xmlrpc.client import Boolean
from messager import *
from player import *
from board import *
from items import *
from os import system
import keyboard
import datetime
import sys

class Game:
    """the game class, includes commands and command processor"""

    attime: str
    ground: list
    
    # defaults
    message: Message = Message(['' for _ in range(4)])
    player: Player = Player()
    actionCount: int = 0
    stage: float = 1.0
    board = Board().board
    
    # initializes with hidden cursor, player at (4, 4)
    def __init__(self) -> None:
        # hide cursor
        print("\x1b[?25l") 
        
        # get item layout
        self.ground = items.itemize()
        
        # update screen
        self._frame(action=False)
        
        # start
        self.process()
    
    # loads a new frame, very important
    def _frame(self, action: bool = True, timer: float = 0.5) -> None:
        # clear
        system('cls')
        
        # the line and action count
        line = f'Action Count: {self.actionCount}\n'
        
        # visual window fo 10x10
        for a in range(self.player.x-5, self.player.x+5):
            for b in range(self.player.y-5, self.player.y+5):
                # done checker
                done = False
                
                # show player over anything
                if (a, b) == (self.player.x, self.player.y):
                        line += repr(self.player)
                        done = True
                
                # show item over empty
                if done is False:
                    for i in self.ground:
                        if (a, b) == (i.x, i.y) and self.stage == i.k:
                            line += repr(i)
                            done = True
                        
                # otherwise, show empty
                if done is False:
                    line += self.board[self.stage][a][b]
                        
            line += '\n'
        
        # if the action tag is active, add action
        if action:
            self.actionCount += timer
        
        # get message lines
        for item in self.message.lines:
            line += f'{item}\n'
        
        # display
        print(line[:-1])

    
    # command processor loop method
    def process(self) -> None:
        # command loop
        while True:
            # time setter
            self.attime = f'{datetime.datetime.now().strftime("%H:%M:%S")}: '
            
            # event reader
            event = keyboard.read_event()
            # event matcher
            match event.name + event.event_type:
                
                case 'wdown':
                    self.goup()
                    
                case 'adown':
                    self.goleft()
                    
                case 'xdown':
                    self.godown()
                    
                case 'ddown':
                    self.goright()
                    
                case 'qdown':
                    self.goupleft()
                
                case 'edown':
                    self.goupright()
                
                case 'zdown':
                    self.godownleft()
                
                case 'cdown':
                    self.godownright()
                
                case '<down':
                    self.climbdown()
                
                case '>down':
                    self.climbup()
                
                case 'sdown':
                    self.restonce()
                    
                case 'gdown':
                    self.grab()
                    
                case 'idown':
                    self.listinv()
                    
                case 'ldown':
                    self.leaveitem()
                
                case 'escdown':
                    self.quit()
    
    # failed to move, reload frame and inform
    def fail(self) -> None:
        self.message.roll(f'{self.attime}You can\'t move there!')
        self._frame(action=False)
    
    # command methods
    #
    # go up
    def goup(self) -> None:
        # checks if it's moving into a wall
        if self.board[self.stage][self.player.x-1][self.player.y] == Board().tiles['wall']:
            # if so, calls fail
            self.fail()
            return
        # otherwise, updates player position
        self.player.x, self.player.y = self.player.x-1, self.player.y  
        # reloads frame      
        self._frame()
    
    # go left
    def goleft(self) -> None:
        if self.board[self.stage][self.player.x][self.player.y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x, self.player.y-1        
        self._frame()
    
    # go down
    def godown(self) -> None:
        if self.board[self.stage][self.player.x+1][self.player.y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x+1, self.player.y        
        self._frame()
    
    # go right
    def goright(self) -> None:
        if self.board[self.stage][self.player.x][self.player.y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x, self.player.y+1        
        self._frame()
    
    # go up left
    def goupleft(self) -> None:
        if self.board[self.stage][self.player.x-1][self.player.y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x-1, self.player.y-1       
        self._frame()
    
    # go up right
    def goupright(self) -> None:
        if self.board[self.stage][self.player.x-1][self.player.y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x-1, self.player.y+1      
        self._frame()
        
    # go down left
    def godownleft(self) -> None:
        if self.board[self.stage][self.player.x+1][self.player.y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x+1, self.player.y-1        
        self._frame()
    
    # go down right
    def godownright(self) -> None:
        if self.board[self.stage][self.player.x+1][self.player.y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x+1, self.player.y+1      
        self._frame()
        
    # down stairs
    def climbdown(self) -> None:
        # checks if there's stairs going down
        if Board().board[self.stage][self.player.x][self.player.y] == Board().tiles['down']:
            # if yes, updates stage
            self.stage += 1
            self.player.x, self.player.y = Board().transdown[self.stage]
            self._frame()
            return
        # otherwise, fails
        self.message.roll(f'{self.attime}Can\'t go down here!')
        self._frame(action=False)
        
    # up stairs
    def climbup(self) -> None:
        if Board().board[self.stage][self.player.x][self.player.y] == Board().tiles['up']:
            self.stage -= 1
            self.player.x, self.player.y = Board().transup[self.stage]
            self._frame()
            return
        self.message.roll(f'{self.attime}Can\'t go up here!')
        self._frame(action=False) 
        
    # grab item
    def grab(self) -> None:
        if self.isfull():
            self.message.roll(f'{self.attime}Your inventory is full!')
            self._frame(action=False)
            return 
        
        for i in self.ground:
            if (self.player.x, self.player.y, self.stage) == (i.x, i.y, i.k):
                self.ground.remove(i)
                self.player.inventory.append(i)
                self.message.roll(f'{self.attime}Grabbed {i.name}')
                self._frame()
                return
        self.message.roll(f'{self.attime}No item here!')
        self._frame(action=False)
        
    # leave item
    def leaveitem(self) -> None:
        if self.isempty():
            self.message.roll(f'{self.attime}You\'re not holding anything!')
            self._frame(action=False)
            return 
        
        if self.isfull():
            self.message.roll(f'{self.attime}Your inventory is full!')
            self._frame(action=False)
            return 
        
        selector = 0
        self.message.roll(f'{self.attime}What item to leave?')
        
        def updateline():
            line = ''
            for i in self.player.inventory:
                if self.player.inventory.index(i) == selector:
                    line += f'\n> {i.type:10} {i.name:10} <'
                else:
                    line += f'\n  {i.type:10} {i.name:10}  '
            self._frame(action=False)
            print(line)
        
        updateline()
        while True:
            event = keyboard.read_event()
            match event.name + event.event_type:
                
                case '.down':
                    if selector == len(self.player.inventory)-1:
                        selector = 0
                    else:
                        selector += 1
                    updateline()
                    
                case 'enterdown':
                    i = self.player.inventory[selector]
                    i.x, i.y, i.k = self.player.x, self.player.y, self.stage
                    self.ground.append(i)
                    self.player.inventory.remove(i)
                    self.message.roll(f'{self.attime}Left {i.name}!')
                    self._frame()
                    break
                
                case 'escdown':
                    self._frame(action=False)
                    break
                
                case _:
                    pass
                
        
    # list inventory
    def listinv(self) -> None:
        if self.isempty():
            self.message.roll(f'{self.attime}You\'re not holding anything!')
            self._frame(action=False)
            return 
        
        mess = ''
        for i in self.player.inventory:
            mess += f'{i.type} {i.name}, '
        mess = mess[:-2]
        
        self.message.roll(f'{self.attime}{mess}')
        self._frame(action=False)
        
    # rest once
    def restonce(self) -> None:
        # reloads taking 1 turn
        self._frame(timer=1)
    
    # quitter
    def quit(self) -> None:
        # reloads
        self.message.roll(f'{self.attime}Press ESC to exit. ')
        self._frame(action=False) 
        
        # event buffer
        keyboard.read_event()
        
        # checks event
        event = keyboard.read_event()
        if event.name == 'esc':
            system('cls')
            sys.exit()
        else:
            self.message.lines[-1] += 'Resuming...'
            self._frame(action=False)

    # empty inventory
    def isempty(self) -> Boolean:
        if self.player.inventory == []:
            return True
        return False
    
    # full inventory
    def isfull(self) -> Boolean:
        if len(self.player.inventory) == 10:
            return True
        return False

# RUN
if __name__ == '__main__':
    game = Game()
