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
    
    title: str
    
    def __init__(self, name: str = '', species: str = '', background: str = '') -> None:
        self.x = 10
        self.y = 10
        self.inventory = []
        self.name = name
        self.species = species
        self.background = background
        self.damage = 0
        self.protection = 0
        
        self.title = f'{self.name}, the {self.species} {self.background}'
        
        if self.species == 'Human':
            self.damage = 1
            self.protection = 1
        if self.species == 'Orc':
            self.damage = 2
            self.protection = 0
        if self.species == 'Elf':
            self.damage = 0
            self.protection = 2
        if self.background == 'Warrior':
            self.damage += 1
        else:
            self.protection += 1

    def __repr__(self) -> str:
        return '@'
    