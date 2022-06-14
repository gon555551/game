class Player:
    """the player"""

    __name: str
    icon: str
    
    def __init__(self) -> None:
        self.__name = None
        self.icon = '@'

    def __repr__(self) -> str:
        return '@'
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    