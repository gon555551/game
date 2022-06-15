import items

"""
The player class, and in the future, the subclasses.
"""

class Player:
    """the player"""
    
    x: int
    y: int
    inventory: list[items.Item]
    
    damage: float
    protection: float
    
    name: str
    species: str
    background: str
    
    def __init__(self, name: str = '', species: str = '', background: str = '') -> None:
        self.x = 10
        self.y = 10
        self.inventory = []
        
        self.damage = 0
        self.protection = 0
        
        self.name = name
        self.species = species
        self.background = background

    def __repr__(self) -> str:
        return '@'
    