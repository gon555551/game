from os import system
import keyboard
import string
from sys import exit

class Lander():
    """landing page"""
    
    species_list: list[str] = [
        'Human',
        'Elf',
        'Orc'
    ]
    background_list: list[str] = [
        'Warrior',
        'Mage'
    ]
    
    place: dict = {
        True: species_list,
        False: background_list
    }
    
    name: str = ''
    species: str = ''
    background: str = ''
    
    line_species: str = ''
    line_background: str = ''
    
    choice: bool = True
    selector: int = 0
    
    
    def __init__(self) -> None:
        self.fresh()                
        self.start()
    
    
    
    def fresh(self) -> None:
        system('cls')
        self.line_changer()

        line = f"""Name: {self.name}

Species: {self.species}{self.line_species}

Background: {self.background}{self.line_background}""" 
        print(line)

    def line_changer(self) -> None:
        if self.choice:
            self.line_species = ''
            for s in self.species_list:
                if self.species_list.index(s) == self.selector:
                    self.line_species += f'\n> {s:10} <'
                else:
                    self.line_species += f'\n  {s:10}  '
            
            self.line_background = ''
            for b in self.background_list:
                self.line_background += f'\n  {b:10}  '
        else:
            self.line_background = ''
            for b in self.background_list:
                if self.background_list.index(b) == self.selector:
                    self.line_background += f'\n> {b:10} <'
                else:
                    self.line_background += f'\n  {b:10}  '
                
    def start(self) -> None:
        while True:
            event = keyboard.read_event()
            
            match event.name + event.event_type:
                case '.down':
                    if self.selector == len(self.place[self.choice])-1:
                        self.selector = 0
                    else:
                        self.selector += 1

                    self.line_changer()
                    self.fresh()
                case 'enterdown':
                    if self.choice:
                        self.species = self.species_list[self.selector]
                        self.choice = not self.choice
                        self.selector = 0
                        self.line_changer()
                        self.fresh()
                    else:
                        self.background = self.background_list[self.selector]
                        self.line_changer()
                        self.fresh()
                        if not self.goOn():
                            break
                case 'escdown':
                    if not self.choice:
                        self.choice = not self.choice
                        self.selector = 0
                        self.line_changer()
                        self.fresh()
                    else:
                        self.leave()
                case 'backspacedown':
                    self.name = self.name[:-1]
                    self.line_changer()
                    self.fresh()
                case _:
                    if len(self.name) == 10:
                        continue
                    elif event.event_type == 'down':
                        if event.name in string.ascii_letters:
                            self.name += event.name
                            self.line_changer()
                            self.fresh()
                    else:
                        continue
    
    def goOn(self) -> bool:
        
        print(f"""
You are {self.name}, the {self.species} {self.background}.

Press ENTER to continue... """)
        
        # event buffer
        keyboard.read_event()
        
        # checks event
        event = keyboard.read_event()
        if event.name == 'enter':
            return False
        else:
            self.fresh()
            return True
    
    def leave(self) -> None:
        print('\nPress ESC to exit... ')
        
        # event buffer
        keyboard.read_event()
        
        # checks event
        event = keyboard.read_event()
        if event.name == 'esc':
            system('cls')
            exit()
        else:
            self.fresh()
