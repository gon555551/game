class Player:
    """the player"""
    
    name: str
    icon: str
    
    def __init__(self, icon: str) -> None:
        self.name = input('what\'s your name? ')
        self.icon = icon