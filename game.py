from data.board import *
from data.player import *
from os import system
import keyboard
import sys

class Game:
    """the game"""
    
    board: list[list]
    player: Player
    
    def __init__(self) -> None:
        self.player = Player()
        self.board = starting_board
        self.frame()
        
        self.board[4][4] = self.player
        self.frame()
        
        self.process()
    
    
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
    
    # load a new frame
    def frame(self) -> None:
        system('cls')
        line = ''
        for a in range(10):
            for b in range(10):
                if self.board[a][b] == self.player:
                    line += repr(self.player)
                else:
                    line += self.board[a][b]
            line += '\n'
        print(line)
    
    
    # command methods
    #
    # go up
    def goup(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x-1][y] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x-1][y] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # go left
    def goleft(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x][y-1] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x][y-1] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # go down
    def godown(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x+1][y] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x+1][y] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # go right
    def goright(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x][y+1] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x][y+1] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # go up and left
    def goupleft(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x-1][y-1] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x-1][y-1] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # go up right
    def goupright(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x-1][y+1] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x-1][y+1] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
        
    # go down and left
    def godownleft(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x+1][y-1] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x+1][y-1] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # go down right
    def godownright(self) -> None:
        coor = [coor for coor in self.board if self.player in coor][0]
        x, y = self.board.index(coor), coor.index(self.player)
        
        if self.board[x+1][y+1] != tiles['empty']:
            self.frame()
            print('Can\'t move there!')
            return
        
        self.board[x+1][y+1] = self.player
        self.board[x][y] = tiles['empty']
        
        self.frame()
    
    # quitter
    def quit(self) -> None:
        self.frame()
        self.exit = input('Do you want to quit (y/N): ')
        match self.exit:
            case 'y':
                sys.exit()
            case 'N':
                self.frame()
            case _:
                self.frame()
                self.quit()
