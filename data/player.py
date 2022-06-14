class Player:
    """the player"""
    
    icon: str
    
    def __init__(self) -> None:
        self.icon = '@'

    def __repr__(self) -> str:
        return '@'
    