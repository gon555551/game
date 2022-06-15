from data.player import *
from data.board import *
from os import system
import keyboard
import sys

class Game:
    """the game"""
    
    player: Player
    actionCount: int
    stage: float = 1.0
    board = Board().board
    
    def __init__(self) -> None:
        print("\x1b[?25l") # hide cursor
        self.actionCount = 0
        
        self.player = Player(4, 4)
        
        self.frame(action=False)
        self.process()
    
    # load a new frame
    def frame(self, action: bool = True, timer: float = 0.5, flip: tuple = (0, 0)) -> None:
        system('cls')
        line = ''
        for a in range(10):
            for b in range(10):
                if (a, b) == (self.player.x, self.player.y):
                    line += repr(self.player)
                else:
                    line += self.board[self.stage][a][b]
            line += '\n'
        print(line[:-1])
        
        if action:
            self.actionCount += timer
        print('Action Count:', self.actionCount)

    
    # command processor
    def process(self) -> None:
        # commands
        while True:
            event = keyboard.read_event()
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
    
    # failed to move
    def fail(self) -> None:
        self.frame(action=False)
        print('Can\'t move there!')
    
    # command methods
    #
    # go up
    def goup(self) -> None:
        if self.board[self.stage][self.player.x-1][self.player.y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x-1, self.player.y        
        self.frame()
    
    # go left
    def goleft(self) -> None:
        if self.board[self.stage][self.player.x][self.player.y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x, self.player.y-1        
        self.frame()
    
    # go down
    def godown(self) -> None:
        if self.board[self.stage][self.player.x+1][self.player.y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x+1, self.player.y        
        self.frame()
    
    # go right
    def goright(self) -> None:
        if self.board[self.stage][self.player.x][self.player.y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x, self.player.y+1        
        self.frame()
    
    # go up and left
    def goupleft(self) -> None:
        if self.board[self.stage][self.player.x-1][self.player.y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x-1, self.player.y-1       
        self.frame()
    
    # go up right
    def goupright(self) -> None:
        if self.board[self.stage][self.player.x-1][self.player.y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x-1, self.player.y+1      
        self.frame()
        
    # go down and left
    def godownleft(self) -> None:
        if self.board[self.stage][self.player.x+1][self.player.y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x+1, self.player.y-1        
        self.frame()
    
    # go down right
    def godownright(self) -> None:
        if self.board[self.stage][self.player.x+1][self.player.y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.player.x, self.player.y = self.player.x+1, self.player.y+1      
        self.frame()
        
    # down stairs
    def climbdown(self) -> None:
        if Board().board[self.stage][self.player.x][self.player.y] == Board().tiles['down']:
            self.stage += 1
            self.frame()
            return
        self.frame(action=False)
        print('Can\'t go down here!')
        
    # up stairs
    def climbup(self) -> None:
        if Board().board[self.stage][self.player.x][self.player.y] == Board().tiles['up']:
            self.stage -= 1
            self.frame()
            return
        self.frame(action=False)
        print('Can\'t go up here!')    
        
    # rest once
    def restonce(self) -> None:
        self.frame(timer=1)
    
    # quitter
    def quit(self) -> None:
        self.frame(action=False) 
        print('Press ESC to exit.')
        keyboard.read_event()
        event = keyboard.read_event()
        if event.name == 'esc':
            sys.exit()
        else:
            self.frame(action=False)


if __name__ == '__main__':
    game = Game()
