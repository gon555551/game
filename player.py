import dataclasses

@dataclasses.dataclass
class Player:
    """the player"""
    
    x: int
    y: int
    inventory: list[tuple]
    
    damage: float
    protection: float
    
    def __init__(self) -> None:
        self.x = 10
        self.y = 10
        self.inventory = []
        
        self.damage = 0
        self.protection = 0

    def __repr__(self) -> str:
        return '@'
    