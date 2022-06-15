import dataclasses
import random

"""
Boards and a few other important sets of information, like tile codes and stair coordinates.
"""

@dataclasses.dataclass
class Board:
    """the boards"""
    
    board: dict
    tiles: dict
    transdown: dict
    transup: dict
    
    def __init__(self) -> None:
        self.board = {
            1: [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '1', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '<', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']],
        
            2: [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '2', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '<', '>', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']],
            
            3: [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '>', '.', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        }
        
        self.tiles = {
            'wall': '#',
            'empty': '.',
            'down': '<',
            'up': '>', 
            'sword': 'S',
            'shield': 'H',
            'many': '='
        } 
        
        self.transdown = {
            2: (14, 13),
            3: (14, 21)
        }
        
        self.transup = {
            1: (14, 13),
            2: (14, 12)
        }
        
        self.generate()

    def buffer(self) -> None:
        for k in self.board.keys():
            buff1 = [['#' for a in range(len(self.board[k][0])+10)] for _ in range(5)]
            buff2 = [['#' for a in range(len(self.board[k][0])+10)] for _ in range(5)]
            for i in range(len(self.board[k])):
                self.board[k][i] = ['#' for _ in range(5)] + self.board[k][i] + ['#' for _ in range(5)]

            for i in range(len(buff2)):
                self.board[k].append(buff2[i])
            for i in range(len(self.board[k])):
                buff1.append(self.board[k][i])
            self.board[k] = buff1
    
    def get_empty(self, num: int) -> list:
        result = []
        for _ in range(num):
            k = random.choice(list(self.board.keys()))
            ok = False
            while not ok:
                y = random.choice(range(len(self.board[k][0])))
                x = random.choice(range(len(self.board[k])))
                if [k, x, y] in result:
                    break
                if self.board[k][x][y] == self.tiles['empty']:
                    ok = True
                    
            result.append([k, x, y])
        
        return result
    
    def getempty_s(self, stage: int) -> tuple:
        while True:
            y = random.choice(range(len(self.board[stage][0])))
            x = random.choice(range(len(self.board[stage])))
            if self.board[stage][x][y] == self.tiles['empty']:
                return (x, y)
    
    def generate(self) -> None:
        self.board[4] = []
        x = random.choice(range(10, 30))
        y = random.choice(range(10, 30))
        for a in range(y):
            line = []
            for b in range(x):
                line.append(random.choice([self.tiles['wall'], self.tiles['empty'], self.tiles['empty']]))
            self.board[4].append(line)
        
        self.buffer()
        
        down = self.getempty_s(4)
        self.transdown[4] = down
        up_3 = self.getempty_s(3)
        self.transup[3] = up_3
        self.board[4][down[0]][down[1]] = self.tiles['up']
        self.board[3][up_3[0]][up_3[1]] = self.tiles['down']
        