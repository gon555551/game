from player import *
from board import *
from os import system
import keyboard
    
class Game:
    """the game"""
    
    board: Board
    player: Player
    exit: str
    
    def __init__(self) -> None:
        self.exit = 'N'
        
        self.board = Board()
        self.frame()
        
        self.player = Player(input('What\'s your name? '), '@')
        
        self.start()
        
        keyboard.add_hotkey('w', self.up)
        keyboard.add_hotkey('esc', self.quit)
        
        while self.exit != 'y':
            pass
        
    def start(self) -> None:
        self.board.board[5][5] = self.player.icon
        self.frame()
        
    def up(self) -> None:
        x = [x for x in self.board.board if self.player.icon in x][0]
        a, b = self.board.board.index(x), x.index(self.player.icon)
        self.board.board[a-1][b] = self.player.icon
        self.board.board[a][b] = '.'
        
        self.frame()
        
    def quit(self) -> None:
        self.exit = input('Do you want to quit (y/N): ')
        match self.exit:
            case 'y':
                pass
            case 'N':
                self.frame()
            case _:
                self.frame()
                self.quit()                    
        
    def frame(self) -> None:
        system('cls')
        for a in range(10):
            line = ''
            for b in range(10):
                line += self.board.board[a][b]
            print(line)
        

if __name__ == '__main__':
    game = Game()
