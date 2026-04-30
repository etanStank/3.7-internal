"""Manage Chapter objects and their lifecycle within a book system."""

from typing import Optional
import os

import states
import book

# Simple tracker to generate unique chapter IDs.
AVAILABLE_ID = 0

# Amount of lines to show in a chapter snippet
SNIPPET_LINES = 3

# Allows for easy retrieval of chapter objects by name,
# and management of registered chapters. Can be expanded
# to allow for data persistency.
REGISTERED_CHAPTERS = []


# -------------------------
# Private Helpers
# -------------------------
def get_available_id() -> int:
    """Return a unique incrementing chapter ID.

    This method uses a simple global counter to ensure that each book
    receives a unique ID upon creation. The counter is incremented each time
    a new book is created. Keeping each unique per session, allowing for easy
    retrieval, and in the future presistent storage if needed.

    Returns:
        int: The next available unique chapter ID.
    """
    global AVAILABLE_ID
    AVAILABLE_ID += 1
    return AVAILABLE_ID


# -------------------------
# Public Method
# -------------------------
def get_chapter_by_name(name: str) -> Optional["Chapter"]:
    """Return a chapter object by its name.

    This method allows for easy retrieval of chapter objects
    based on their title, this allows for easy searching and
    management of chapters.

    Returns:
        Optional[Chapter]: The chapter object with the matching name, 
        or None if not found.
    """
    name = name.lower()

    for chapter in REGISTERED_CHAPTERS:
        # Loops through REGISTERED_CHAPTERS
        # Checking if a chapter with the same name exists
        # Returning if so, if not returning None
        if chapter._title.lower() == name:
            return chapter

    return None


def get_chapter_title(title: str) -> str:
    """Return a filename without its extension.

    This method allows for the extraction of a chapter
    title from the original filename, regardless of what
    file extension was used. Allowing for more flexible file
    types to be used in the future.

    Returns:
        str: The chapter title extracted from the filename.
    """
    # Fancy way to get the filename without any
    # extensions, regardless of the extension
    return os.path.splitext(title)[0]


# -------------------------
# Chapter Class
# -------------------------
class Chapter:
    """Represent a single chapter within a book.

    Each chapter has a unique ID, title, and file. This,
    allows for easy management and retrieval of chapter information,
    Each chapter has an attached state observers that can be used to track,
    the chapter's current state, and fire actions based on the state change.
    The lines included in the raw (after being processed) are stored ina list,
    allowing for easy retrieval later on. Along with this the chapter has a
    stats dictionary, which allows for easy storage and retrieval of various stats
    related to the chapter, such as character count, line count, etc. A dictionary
    allows for more to be added in the future without needing to change the class structure.
    Alongside being able to directly get the stat with only using the name of the stat.

    """

    def __init__(self, name: str, raw: str, book_name: str) -> None:
        """Initialize a Chapter object.

        Args:
            name (str): The original filename of the chapter.
            raw (str): The raw text content of the chapter.
            book_name (str): The name of the book this chapter belongs to.
        """
        # Immutaable attributes
        self._id = get_available_id()
        self._file = name
        self._title = get_chapter_title(name)
        self._raw = raw

        # Mutable attributes
        self.book = None
        self.lines = []
        self.stats = {}

        # State attributes
        self._state = "Initializing"
        self._observers = []

        # Initialization
        self._initialize(book_name)

    def __repr__(self) -> str:
        """Return a developer-friendly string representation.

        This method provides a clear and concise
        representation of the chapter object, including its
        unique ID and file, title, and state.
        This is useful for debugging purposes.

        Returns:
            str: A string representation of the chapter object.
        """
        return (
            f"Chapter(id={self._id}, file='{self._file}', "
            f"title='{self._title}', state='{self._state}')"
        )

    # -------------------------
    # Properties
    # -------------------------
    @property
    def id(self) -> int:
        """Return the book's unique ID.

        This property allows for easy retrieval of
        the book's unique identifier, which can be used
        for various operations such as searching or
        referencing the chapter.

        Returns:
            int: The unique ID of the chapter.
        """
        return self._id

    @property
    def title(self) -> str:
        """Return the chapter's title.

        This property allows for easy retrieval
        of the chapters title, which can be used for
        terminal purposes, or searching for the chapter.

        Returns:
            str: The title of the chapter.
        """
        return self._title

    # -------------------------
    # Content Methods
    # -------------------------
    def get_snippet(self) -> str:
        """Get the first designed amount of lines.

        This method allows for easy retrieval of a snippet
        of the chapter content, which can allow the user to
        get a preview of the chapter without having to commit to
        reading it.

        Returns:
            str: A snippet of the chapter content.
        """
        snippet = self.lines[:SNIPPET_LINES]
        return "\n".join(snippet)

    # -------------------------
    # State Management
    # -------------------------
    @property
    def state(self) -> str:
        """Return the current state.

        This method allows for easy retrieval of the chapter's
        current state.

        Returns:
            str: The current state of the chapter.
        """
        return self._state

    def set_state(self, state: str) -> str:
        """Set the current state and notify observers.

        This method allows for the chapter's state to be updated,
        to a specific state, and notifies all attached observers.
        This is used instead of next_state when a specific state
        needs to be set, such as in testing, or when initializing.

        Args:
            state (str): The new state to set for the chapter.

        Returns:
            str: The updated state after changing, or None.
        """
        self._state = state
        self._event()
        return self._state

    def next_state(self) -> Optional[str]:
        """Transition to the next state, and notify observers.

        This method allows for the chapter's state to be updated,
        to the next state in the defined state positions, and notifies
        the attached observers. This is used to progress through the
        chapter's initializing, and processings. This is used instead of
        set_state when the chapter is going through the standard flow.

        Returns:
            str: The updated state after changing, or None.
        """
        # Current state index found in the STATE_POSITIONS table in states.py
        current_state_index = states.STATE_POSITIONS.index(self._state)
        next_state_index = current_state_index + 1

        if current_state_index < len(states.STATE_POSITIONS):
            # Checks if next_state_index is within the bounds of the
            # STATE_POSITIONS table, if so it gets the next state
            if states.STATE_POSITIONS[next_state_index]:
                # Updates the chapter's state to the next state, and
                # notifies the observers of the state change
                self._state = states.STATE_POSITIONS[next_state_index]
                self._event()
                return self._state
            else:
                return None
        else:
            return None

    # -------------------------
    # Stats
    # -------------------------
    def set_stats(self, new_stats: dict) -> None:
        """Replace all stats with a new dictionary.

        This method allows for the chapter's state to be set
        at once, this is mainly used in initialization, but can
        also be used to reset the stats if needed.

        Args:
            new_stats (dict): A dictionary containing the new stats.
        """
        self.stats = new_stats

    def set_stat(self, stat_name: str, stat_value) -> None:
        """Set a specific stat value.

        This method allows for a specific stat to be updated or added
        without needing to replace the entire stats dictionary. This is useful
        for updating specifici stats if they are re-caculated, or new.

        Args:
            stat_name (str): The name of the stat to set.
            stat_value: The value of the stat to set.
        """
        self.stats[stat_name] = stat_value

    def get_stat(self, stat_name: str) -> Optional[str | int]:
        """Return a specific stat value if it exists.

        This method allows for easy retrieval of specific stats
        using their stat_name.

        Args:
            stat_name (str): The name of the stat to get.

        Returns:
            str | int: The value of the stat if it exists, or None.
        """
        return self.stats.get(stat_name)

    # -------------------------
    # Observer Pattern
    # -------------------------
    def attach(self, observer: object) -> None:
        """Attach an observer.

        This method allows for easy attachment of observer objects
        to a specific chapter. This allows for the chapter to easily
        manage the observers of state changes, and fire methods.

        Args:
            observer (object): The observer object to attach.
        """
        self._observers.append(observer)

    def detach(self, observer: object) -> None:
        """Detach an observer.
        
        This method allows for easy detachment of observer objects
        to a specific chapter. This allows for the chapter to easily
        manage the observers of state changes, and fire methods.

        Args:
            observer (object): The observer object to detach.
        """
        self._observers.remove(observer)

    def _event(self) -> None:
        """Notify all observers of a state change.
        
        This method allows for the chapter to notify / fire
        methods on all attached observers when a state change occurs.
        """
        for observer in self._observers:
            # Loops through all observers, and runs the .update method
            observer.update(self, self._state)

    # -------------------------
    # Initialization
    # -------------------------
    def _initialize(self, book_name: str) -> None:
        """Set up the chapter and register it.
        
        This method is called during the chapter's internal
        intialization process, and allows for all of the necessary
        setup to be done in one place, instead of in states.py

        Args:
            book_name (str): The name of the book this chapter belongs to.
        """
        REGISTERED_CHAPTERS.append(self)

        # Gets the book object
        book_object = book.get_book(book_name or "Unknown")

        # Sanity check to make sure the book exists
        if book_object:
            self.book = book_object
            book_object.add_chapter(self)

        # Attaches all states to the chapter
        for state in states.READY_STATES:
            self.attach(state)

        # !Can be removed in the future, just for testing! - note to self.
        print("Initialization of Chapter complete.")

        # Allows for the chapter to progess to the next state
        self.next_state()