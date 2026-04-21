""" 

No idea what todo with this yet.
Wrote this before thinking about my weird
"state observing" design pattern, whatever.

"""

from dataclasses import dataclass
from typing import Optional

AVAILABLE_ID = 0
AVAILABLE_BOOKS = []
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

        AVAILABLE_BOOKS.append(self)
    
    def __repr__(self) -> str:
        return f"Book(id={self._id}, name='{self._name}')"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    def AddChapter(self, chapterObject: object):
        self.chapters.append(chapterObject)


    
# Public Methods
def getBook(name: str) -> Optional[Book]:
    for book in AVAILABLE_BOOKS:
        if book.name == name:
            return book
    packet = bookCreation(name, [])
    return Book(packet)

def getBooks() -> list:
    return AVAILABLE_BOOKS

def getBookById(id: int) -> Optional[object]:
    for book in AVAILABLE_BOOKS:
        if book.id == id:
            return book
    return None    