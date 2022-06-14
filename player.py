class Player:
    """the player"""
    
    name: str
    icon: str
    
    def __init__(self, name: str, icon: str) -> None:
        self.name = name
        self.icon = icon
