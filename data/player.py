import dataclasses

@dataclasses.dataclass
class Player:
    """the player"""
    
    x: int
    y: int

    def __repr__(self) -> str:
        return '@'
    