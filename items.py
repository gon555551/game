import board

class Item:
    """the items"""
    
    type: str
    
    def __init__(self, type: str) -> None:
        self.type = type

class Sword(Item):
    """swords"""
    
    id: int
    name: str
    x: int
    y: int
    k: int
    
    def __init__(self, id: int, name: str, x, y, k) -> None:
        super().__init__('sword')
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.k = k
        
    def __repr__(self) -> str:
        return 'S'

class Shield(Item):
    """shields"""
    
    id: int
    name: str
    x: int
    y: int
    k: int
    
    def __init__(self, id: int, name: str, x, y, k) -> None:
        super().__init__('shield')
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.k = k
    
    def __repr__(self) -> str:
        return 'H'


def itemize() -> tuple:
    result = board.Board().get_empty(2)
    returned = []
    
    sword = Sword(0, 'JOSEPHINE', result[0][1], result[0][2], result[0][0])
    shield = Shield(1, 'JASPER', result[1][1], result[1][2], result[1][0])
    returned.append(sword)
    returned.append(shield)
    return returned
