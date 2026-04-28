print("Chapter Loaded")

from optparse import Option
from typing import Optional

import os

import states
import book
AVAILABLE_ID = 0
SNIPPET_LINES = 3

REGISTERED_CHAPTERS = []

# Private Methods
def remove_duplications(given_list: list):
    seen = set()
    result = []
    for item in given_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def GetAvailableId() -> int:
    global AVAILABLE_ID
    AVAILABLE_ID = AVAILABLE_ID + 1
    return AVAILABLE_ID

# Public Methods
def GetChapterByName(name: str) -> Optional[Chapter]:
    """Gets a chapter object by its name

    Args:
        name (str): Name of chapter to get

    Returns:
        Optional[object]: Chapter object if found, None if not found
    """
    name = name.lower()
    for chapter in REGISTERED_CHAPTERS:
        if chapter._title.lower() == name:
            return chapter
    return None

def GetChapterTitle(title: str) -> str:
    return os.path.splitext(title)[0]

# Constructor
class Chapter():
    def __init__(self, name: str, raw: str, book: str) -> None:
        """Object init method

        Args:
            name (str): Name of chapter
            raw (str): Raw string of chapter
            book (str): Assosicated book
        """

        for chapter in REGISTERED_CHAPTERS:
            if chapter._title == name:
                print(f"Chapter with title '{name}' already exists.")
                return

        # ID
        self._id = GetAvailableId() # Incase I need todo equality overrides
        self._file = name # TODO: Could remove
        self._title = GetChapterTitle(name)

        self._raw = raw # Only added if needed
        self.book = None # Overall book the chapter is in
        self.lines = [] # Line objects or multidimensional
        self.stats = {} # Stats of chapter, like word count, etc

        # State 
        self._state = "Initializing" # Initializing, Preparing, Ready
        self._observers = []
        self.initializing()

    def __repr__(self) -> str:
        return f"Chapter(id={self._id}, file='{self._file}', title='{self._title}', state='{self._state}')"
    
    """ -- Properties -- """
    @property
    def id(self) -> int:
        """Gets the chapter's ID 

        Returns:
            int: Chapter's ID
        """
        return self._id
    
    @property
    def title(self) -> str:
        """Gets the chapter's title

        Returns:
            str: Chapter's title
        """
        return self._file

    def getSnippet(self) -> str:
        snippet = []
        for turn in range(SNIPPET_LINES):
            snippet.append(self.lines[turn])
        
        return "\n".join(snippet)


    """ -- States -- """
    @property
    def state(self) -> str:
        """Gets the current state of the chapter

        Returns:
            str: State name
        """
        return self._state
    
    def setState(self, state: str) -> str:
        """Sets the current state to a new state

        Args:
            state (str): New state name

        Returns:
            str: Updated state name
        """
        self._state = state
        self.event() # Updates all states
        return self._state
    
    def setStats(self, new_stats: dict) -> None:
        """Sets the chapter's stats

        Args:
            new_stats (dict): New stats to set
        """
        self.stats = new_stats

    """ -- Chapter Stats -- """
    def setStat(self, stat_name: str, stat_value) -> None:
        """Sets a specific stat of the chapter

        Args:
            stat_name (str): Name of stat to set
            stat_value (Any): Value of stat to set
        """
        self.stats[stat_name] = stat_value

    def getStat(self, stat_name: str) -> Optional[str | int]:
        """Gets a specific stat of the chapter

        Args:
            stat_name (str): Name of stat to get

        Returns:
            Any: Value of stat, or None if not found
        """
        return self.stats.get(stat_name, None)
    
    """ -- Observers -- """
    def attach(self, observer: object) -> None:
        """Attaches a new state observer

        Args:
            observer (object): State observer
        """
        self._observers.append(observer)
    
    def detach(self, observer: object) -> None:
        """Detachs a current state observer

        Args:
            observer (object): State observer
        """
        self._observers.remove(observer)

    def event(self) -> None:
        """Sends an update to each observer

        """
        for observer in self._observers:
            status = observer.update(self, self._state)
            if status == "Callable":
                print("Successfully changed observers state")
            elif status == "Not callable":
                print("Error occured while changing observers state")

    """ -- Init -- """
    def initializing(self) -> None:
        """Initializes chapter object logic
        """

        # Temporary fix till I figure out why its duplicated
        # Like what and why
        REGISTERED_CHAPTERS.append(self)
        remove_duplications(states.ready_states) 
        print(states.ready_states)
        book_object = book.getBook("Unknown")
        if book_object:
            self.book = book_object
            book_object.AddChapter(self)
        
        print(book.getBooks())

        for state in states.ready_states:
            self.attach(state)
        
        print("Initialization of Chapter complete.")
        self.setState("Preparing")