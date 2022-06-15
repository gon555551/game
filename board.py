import dataclasses
import items
import random

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
        
        self.buffer()

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
    
    def get_empty(self, num: int) -> tuple:
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