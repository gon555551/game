import board

class Item:
    """the items"""
    
    type: str
    
    damage: float
    protection: float
    
    def __init__(self, type: str, damage: float, protection: float) -> None:
        self.type = type
        self.damage = damage
        self.protection = protection

class Sword(Item):
    """swords"""
    
    id: int
    name: str
    x: int
    y: int
    k: int
    
    def __init__(self, id: int, name: str, x, y, k, damage) -> None:
        super().__init__('sword', damage, 0)
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
    
    def __init__(self, id: int, name: str, x, y, k, prot) -> None:
        super().__init__('shield', 0, prot)
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
    
    sword = Sword(0, 'JOSEPHINE', result[0][1], result[0][2], result[0][0], 5)
    shield = Shield(1, 'JASPER', result[1][1], result[1][2], result[1][0], 5)
    returned.append(sword)
    returned.append(shield)
    return returned
