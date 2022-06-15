import dataclasses

"""
Handles the message line.
"""

@dataclasses.dataclass
class Message:
    """message lines"""
    
    lines: list[str]
    
    def roll(self, message: str) -> None:
        self.lines = self.lines[1:]
        self.lines.append(message)
    