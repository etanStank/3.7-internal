""" 

No idea what todo with this yet.
Wrote this before thinking about my weird
"state observing" design pattern, whatever.

"""

from dataclasses import dataclass
from typing import Optional

AVAILABLE_ID = 0

# Types

@dataclass
class bookCreation:
    name: str
    chapters: list

# Private Methods

def GetAvailableId() -> int:
    global AVAILABLE_ID
    AVAILABLE_ID = AVAILABLE_ID + 1
    return AVAILABLE_ID

# Constructor

class Book():
    def __init__(self, packet: bookCreation) -> None:
        # Immutable
        self._id = GetAvailableId()
        self._name = packet.name

        # Mutable          
        self.chapters = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    def AddChapter(self, chapterObject: object):
        pass


    
# Public Methods

def findBook(name: str) -> Optional[object]:
    return False