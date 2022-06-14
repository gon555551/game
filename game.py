from data.player import *
from data.board import *
from os import system
import keyboard
import sys

class Game:
    """the game"""
    
    board: list[list]
    player: Player
    actionCount: int
    stage: int
    
    def __init__(self) -> None:
        self.actionCount = 0
        self.stage = 2
        
        self.player = Player()
        self.board = Board().board[self.stage]
        
        self.frame(action=False)
        
        self.board[4][4] = self.player
        self.frame(action=False)
        
        self.process()
    
    # load a new frame
    def frame(self, action: bool = True) -> None:
        print("\x1b[?25l") # hide cursor
        system('cls')
        line = ''
        for a in range(10):
            for b in range(10):
                if self.board[a][b] == self.player:
                    line += repr(self.player)
                else:
                    line += self.board[a][b]
            line += '\n'
        print(line[:-1])
        
        if action:
            self.actionCount += 1
        print('Action Count:', self.actionCount)
        
        print(Board().board[self.stage])
    

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
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x-1][y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x-1][y] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go left
    def goleft(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x][y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x][y-1] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go down
    def godown(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x+1][y] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x+1][y] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go right
    def goright(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x][y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x][y+1] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go up and left
    def goupleft(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x-1][y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x-1][y-1] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go up right
    def goupright(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x-1][y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x-1][y+1] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
        
    # go down and left
    def godownleft(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x+1][y-1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x+1][y-1] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # go down right
    def godownright(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x+1][y+1] == Board().tiles['wall']:
            self.fail()
            return
        
        self.board[x+1][y+1] = self.player
        self.board[x][y] = Board().board[self.stage][x][y]
        
        self.frame()
    
    # quitter
    def quit(self) -> None:
        self.frame(action=False)
        print("\x1b[?25h") # show cursor 
        self.exit = input('Do you want to quit (y/N): ')
        match self.exit:
            case 'y':
                sys.exit()
            case 'N':
                self.frame(action=False)
            case _:
                self.frame(action=False)
                self.quit()
