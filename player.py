import dataclasses

@dataclasses.dataclass
class Player:
    """the player"""
    
    x: int
    y: int
    inventory: list[tuple]
    
    def __init__(self) -> None:
        self.x = 10
        self.y = 10
        self.inventory = []

    def __repr__(self) -> str:
        return '@'
    