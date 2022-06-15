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
        self.actionCount = 0
        
        self.player = Player()
        
        self.frame(action=False)
        
        self.board[self.stage][4][4] = self.player
        self.frame(action=False)
        
        self.process()
    
    # load a new frame
    def frame(self, action: bool = True, timer: float = 0.5) -> None:
        print("\x1b[?25l") # hide cursor
        system('cls')
        line = ''
        for a in range(10):
            for b in range(10):
                if self.board[self.stage][a][b] == self.player:
                    line += repr(self.player)
                else:
                    line += self.board[self.stage][a][b]
            line += '\n'
        print(line[:-1])
        
        if action:
            self.actionCount += timer
        print('Action Count:', self.actionCount)
        
    # change stages
    def stager(self, stage: int):
        x, y = self.coords()
        self.stage = stage
        self.board[self.stage][x][y] = self.player
    
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
                case 'sdown':
                    self.restonce()
                case 'escdown':
                    self.quit()
    
    # failed to move
    def fail(self) -> None:
        self.frame(action=False)
        print('Can\'t move there!')
        
    # get coords
    def coords(self) -> tuple:
        coor = [coor for coor in self.board[self.stage] if self.player in coor][0]
        x, y = self.board[self.stage].index(coor), coor.index(self.player)
        return x, y
    
    # command methods
    #
    # go up
    def goup(self) -> None:
        self.board[self.stage]
        x, y = self.coords()
        
        if self.board[self.stage][x-1][y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x-1][y] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go left
    def goleft(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x][y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x][y-1] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go down
    def godown(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x+1][y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x+1][y] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go right
    def goright(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x][y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x][y+1] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go up and left
    def goupleft(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x-1][y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x-1][y-1] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go up right
    def goupright(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x-1][y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x-1][y+1] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
        
    # go down and left
    def godownleft(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x+1][y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x+1][y-1] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go down right
    def godownright(self) -> None:
        x, y = self.coords()
        
        if self.board[self.stage][x+1][y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[self.stage][x+1][y+1] = self.player
        self.board[self.stage][x][y] = Board().board[self.stage][x][y]
        
        self.frame()
        
    # rest once
    def restonce(self) -> None:
        self.frame(timer=1)
    
    # quitter
    def quit(self) -> None:
        self.frame(action=False) 
        self.exit = input('\x1b[?25hDo you want to quit (y/N): ')
        match self.exit:
            case 'y':
                sys.exit()
            case 'N':
                self.frame(action=False)
            case _:
                self.frame(action=False)
                self.quit()


if __name__ == '__main__':
    game = Game()
