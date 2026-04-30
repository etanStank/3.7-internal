"""Basic book management module."""

from dataclasses import dataclass
from typing import Optional, List

# Allows for quick global retrieval of book objects
# Through their name or ID, without needing to
# externally save, or keep data persistently in memory.
AVAILABLE_BOOKS = []

# Simple tracker to generate unique book IDs.
AVAILABLE_ID = 0


# Data Structure
@dataclass
class BookCreation:
    """Data packet used to initialize a Book instance.

    Easily allows for greater range of attributes /
    parameters to be added in the future without needing
    to change the Book class constructor.
    """

    name: str
    chapters: list


# -------------------------
# Private Methods
# -------------------------
def get_available_id() -> int:
    """Generate and return the next available unique book ID.

    This method uses a simple global counter to ensure that each book
    receives a unique ID upon creation. The counter is incremented each time
    a new book is created. Keeping each unique per session, allowing for easy
    retrieval, and in the future presistent storage if needed.

    Returns:
        int: The next available unique book ID.
    """
    global AVAILABLE_ID
    AVAILABLE_ID = AVAILABLE_ID + 1
    return AVAILABLE_ID


# Class Constructor
class Book:
    """Represent a book with a unique ID, name, and chapters.

    Each book has a unique ID generated upon creation, a name
    provided by the text, and a list of chapters that can be
    added to the book. The class provides methods for
    retrieving book information and managing its chapters easily.
    """

    def __init__(self, packet: BookCreation) -> None:
        """Initialize book class.

        Args:
            packet (BookCreation): Packet relating to book creation.
        """
        # Immutable attributes
        self._id = get_available_id()
        self._name = packet.name

        # Mutable attributes
        self.chapters = []

        # Register this object globally
        AVAILABLE_BOOKS.append(self)

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the Book.

        This method provides a clear and concise
        representation of the Book object, including its
        unique ID and name. This is useful for debugging purposes.

        Returns:
            str: A string representation of the chapter object.
        """
        return (
            f"Book(id={self._id}, "
            f"name='{self._name}')"
        )

    @property
    def id(self) -> int:
        """Return the book's unique ID.

        This property allows for easy retrieval of
        the book's unique identifier, which can be used
        for various operations such as searching or
        referencing the book.

        Returns:
            int: Book's unique ID
        """
        return self._id

    # -------------------------
    # Properties
    # -------------------------
    @property
    def name(self) -> str:
        """Return the book's name.

        This property allows for easy retrieval
        of the book's name, which can be used for
        terminal purposes, or searching for the book.

        Returns:
            str: Book's name
        """
        return self._name

    def add_chapter(self, chapter_object: object):
        """Add a chapter object to the book.

        Allows for easy management of the book's chapters by providing a method to add
        chapter objects to the book's chapter list. This method can be used to build
        the book's content dynamically as chapters are processed and created.

        Args:
            chapter_object (str): Chapter object
        """
        self.chapters.append(chapter_object)


# -------------------------
# Public Methods
# -------------------------
def get_book(name: str) -> Optional[Book]:
    """Retrieve a book by name.

    This method checks if a book with the given name already exists in the global
    list of available books. If it does, it returns that book. If not, it creates a new
    book with the provided name, registers it globally, and returns the new book instance.

    Args:
        name (str): The name of the book to retrieve or create.

    Returns:
        Optional[Book]: Book if found, else None
    """
    for book in AVAILABLE_BOOKS:
        # Loops through AVAILABLE_BOOKS
        # Checking if a book with the same name exists
        # Returning if so, if not returning None
        if book.name == name:
            return book

    packet = BookCreation(name, [])
    return Book(packet)


def get_books() -> List[Book]:
    """Return a list of all available books.

    This method provides a way to retrieve all book objects that have been created
    and registered in the global list. This can be useful for displaying available books,
    or for operations that need to access all books in the system.

    Returns:
        List[Book]: List of all books
    """
    return AVAILABLE_BOOKS


def get_book_by_id(book_id: int) -> Optional[Book]:
    """Retrieve a book by its unique ID.

    This method allows for retrieval of a book based on its unique identifier. It iterates
    through the global list of available books and returns the book that matches the provided ID.
    If no book with the given ID is found, it returns None.

    Returns:
        Optional[Book]: Book if found, else None
    """
    for book in AVAILABLE_BOOKS:
        # Loops through AVAILABLE_BOOKS
        # Checking if a book with the same ID exists
        # Returning if so, if not returning None
        if book.id == book_id:
            return book
    return None
