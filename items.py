import board
import random


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

    sym: str = "S"

    def __init__(self, id: int, name: str, x, y, k, damage) -> None:
        super().__init__("sword", damage, 0)
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.k = k

    def __repr__(self) -> str:
        return "S"


class Shield(Item):
    """shields"""

    id: int
    name: str
    x: int
    y: int
    k: int

    sym: str = "H"

    def __init__(self, id: int, name: str, x, y, k, prot) -> None:
        super().__init__("shield", 0, prot)
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.k = k

    def __repr__(self) -> str:
        return "H"


def itemize(board: board.Board, num: int) -> tuple:
    result = board.get_empty(num)
    returned = []
    id = 0

    for i in result:
        tp = random.choice(Item.__subclasses__())
        returned.append(tp(id, f"{id}", i[1], i[2], i[0], random.randint(1, 10)))
        id += 1

    return returned
