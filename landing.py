from os import system
import keyboard
import string
from sys import exit


class Lander:
    """landing page"""

    species_list: list[str] = ["Human", "Elf", "Orc"]
    background_list: list[str] = ["Warrior", "Mage"]
    options_list: list[str] = ["Start", "Controls", "Setup"]

    place: dict = {0: species_list, 1: background_list, 2: options_list}

    on_bg: str = "  "
    on_sp: str = "  "
    on_op: str = "  "

    name: str = ""

    species: str = ""
    background: str = ""
    options: str = ""

    boards: str = "3"
    items: str = "10"

    line_species: str = ""
    line_background: str = ""
    line_options: str = ""

    choice: int = 0
    selector: int = 0

    reading: bool = False

    tinkering: bool = False
    on_bn: str = "  "
    on_in: str = "  "
    bn: bool = True

    def __init__(self) -> None:
        self.fresh()
        self.start()

    def fresh(self) -> None:
        system("cls")
        self.line_changer()

        line = f"""Name: {self.name}

{self.on_sp}Species: {self.species}{self.line_species}

{self.on_bg}Background: {self.background}{self.line_background}

{self.on_op}Options: {self.line_options}

.     ->     move cursor
ENTER ->     select
ESC   ->     go back

Just type your name! 10 characters maximum..."""
        print(line)

    def line_changer(self) -> None:
        if self.choice == 0:
            self.on_bg = "  "
            self.on_op = "  "
            self.on_sp = "* "

            self.line_species = ""
            for s in self.species_list:
                if self.species_list.index(s) == self.selector:
                    self.line_species += f"\n> {s:10} <"
                else:
                    self.line_species += f"\n  {s:10}  "

            self.line_background = ""
            for b in self.background_list:
                self.line_background += f"\n  {b:10}  "

            self.line_options = ""
            for o in self.options_list:
                self.line_options += f"\n  {o:10}  "

        elif self.choice == 1:
            self.on_sp = "  "
            self.on_op = "  "
            self.on_bg = "* "
            self.line_background = ""
            for b in self.background_list:
                if self.background_list.index(b) == self.selector:
                    self.line_background += f"\n> {b:10} <"
                else:
                    self.line_background += f"\n  {b:10}  "

            self.line_options = ""
            for o in self.options_list:
                self.line_options += f"\n  {o:10}  "

        else:
            self.on_bg = "  "
            self.on_sp = "  "
            self.on_op = "* "
            self.line_options = ""
            for b in self.options_list:
                if self.options_list.index(b) == self.selector:
                    self.line_options += f"\n> {b:10} <"
                else:
                    self.line_options += f"\n  {b:10}  "

    def start(self) -> None:
        while True:
            event = keyboard.read_event()

            if self.tinkering:
                match event.name + event.event_type:
                    case "escdown":
                        self.boards = "3"
                        self.items = "10"
                        self.bn = True
                        self.tinkering = False
                        self.line_changer()
                        self.fresh()
                    case ".down":
                        self.bn = not self.bn
                        self.tinker()
                    case "enterdown":
                        break
                    case "backspacedown":
                        if self.bn:
                            self.boards = self.boards[:-1]
                            self.tinker()
                        else:
                            self.items = self.items[:-1]
                            self.tinker()
                    case _:
                        if event.event_type == "down":
                            if event.name in string.digits:
                                if self.bn:
                                    if len(self.boards) < 2:
                                        self.boards += event.name
                                        self.tinker()
                                else:
                                    if len(self.items) < 2:
                                        self.items += event.name
                                        self.tinker()

            elif self.reading:
                match event.name + event.event_type:
                    case "escdown":
                        self.reading = False
                        self.line_changer()
                        self.fresh()
                    case _:
                        pass
            else:
                match event.name + event.event_type:
                    case ".down":
                        if self.selector == len(self.place[self.choice]) - 1:
                            self.selector = 0
                        else:
                            self.selector += 1

                        self.line_changer()
                        self.fresh()
                    case "enterdown":
                        if self.choice == 0:
                            self.species = self.species_list[self.selector]
                            self.choice += 1
                            self.selector = 0
                            self.line_changer()
                            self.fresh()
                        elif self.choice == 1:
                            self.background = self.background_list[self.selector]
                            self.choice += 1
                            self.selector = 0
                            self.line_changer()
                            self.fresh()
                        else:
                            self.options = self.options_list[self.selector]
                            self.line_changer()
                            self.fresh()
                            if not self.goOn():
                                break
                    case "escdown":
                        if self.choice == 2:
                            self.choice -= 1
                            self.selector = 0
                            self.line_changer()
                            self.fresh()
                        elif self.choice == 1:
                            self.choice -= 1
                            self.selector = 0
                            self.line_changer()
                            self.fresh()
                        else:
                            self.leave()
                    case "backspacedown":
                        self.name = self.name[:-1]
                        self.line_changer()
                        self.fresh()
                    case _:
                        if len(self.name) == 10:
                            continue
                        elif event.event_type == "down":
                            if event.name in string.ascii_letters:
                                self.name += event.name
                                self.line_changer()
                                self.fresh()
                        else:
                            continue

    def goOn(self) -> bool:
        if self.options == "Start":
            print(
                f"""
>>>>{'':5}You are {self.name}, the {self.species} {self.background}.{'':5}<<<<

Press ENTER to continue... """
            )
            # event buffer
            keyboard.read_event()

            # checks event
            event = keyboard.read_event()
            if event.name == "enter":
                return False
            else:
                self.fresh()
                return True

        elif self.options == "Controls":
            self.showcontrols()
            return True

        else:
            self.tinker()
            return True

    def leave(self, tink: bool = False) -> None:
        print("\nPress ESC to exit... ")

        # event buffer
        keyboard.read_event()

        # checks event
        event = keyboard.read_event()
        if event.name == "esc":
            system("cls")
            exit()
        else:
            self.fresh()

    def showcontrols(self) -> bool:
        self.reading = True
        system("cls")
        line = """q w e
 \\|/
a-s-d    <- directional movement (0.5) and rest (1.0)
 /|\\
z x c

i       ->       view inventory
g       ->       grab item
l       ->       leave item
v       ->       view items at location
p       ->       get stats
<       ->       go down stairs
>       ->       go up stairs
.       ->       scroll
ENTER   ->       select
ESC     ->       exit the game

"""
        line += """Press ESC to return... """
        print(line)

    def tinker(self) -> None:
        self.tinkering = True
        system("cls")

        def changer() -> None:
            if self.bn:
                self.on_bn = "* "
                self.on_in = "  "
            else:
                self.on_bn = "  "
                self.on_in = "* "

        changer()

        line = f""">>>>{'':5}You are {self.name}, the {self.species} {self.background}.{'':5}<<<<

{self.on_bn}Board Number: {self.boards}
{self.on_in}Item Number:  {self.items}

Press ENTER to advance...
"""
        print(line)
