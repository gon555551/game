from messager import *
from player import *
from board import *
from os import system
import keyboard
import datetime
import sys

class Game:
    """the game class, includes commands and command processor"""
    
    message: Message
    player: Player
    actionCount: int
    attime: str
    stage: float = 1.0
    board = Board().board
    
    # initializes with hidden cursor, actioncount at 0, player at (4, 4)
    def __init__(self) -> None:
        print("\x1b[?25l") # hide cursor
        self.actionCount = 0
        
        self.player = Player(4, 4)
        self.message = Message(['' for _ in range(4)])
        
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
        
        # board
        for a in range(len(self.board[self.stage])):
            for b in range(len(self.board[self.stage][0])):
                # if it's the player, print the player
                if (a, b) == (self.player.x, self.player.y):
                    line += repr(self.player)
                else:
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
            sys.exit()
        else:
            self.message.lines[-1] += 'Resuming...'
            self._frame(action=False)


# RUN
if __name__ == '__main__':
    game = Game()
