class Board:
    """the board"""
    board: list
    
    def __init__(self) -> None:
        self.board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                      ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        