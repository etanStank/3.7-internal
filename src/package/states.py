"""

TODO: Fix duplication, like why. Could add
      equality override worst case scenario
      Why do I always overcomplicate stuff.
"""


print("States Loaded")

from typing import Optional
from typing import TYPE_CHECKING
from dataclasses import dataclass

@dataclass
class ChapterType():
    _id: int
    _file: str
    _title: str
    _raw: str
    book: str
    lines: list
    stats: dict
    _state: str
    _observers: list
    attach: function
    getStat: function
    getSnippet: function
    setState: function
    

ready_states = []

def newState(name: str) -> Optional[State]:
    """Creates a new state object, and adds it to the ready states list

    Args:
        name (str): Name of state

    Returns:
        State: State object created
    """
    for state in ready_states:
        if state._name == name:
            raise ValueError(f"State with name '{name}' already exists.")
            return None

    new_state = State(name)
    ready_states.append(new_state)
    return new_state

# Private Methods
def getLines(raw: str) -> list:
    """Splits a raw string into lines

    Args:
        raw (str): Raw string

    Returns:
        list: List of lines
    """
    lines=  []

    raw_lines = raw.split('\n')
    for line in raw_lines:
        line = line.strip()
        if line:
            lines.append(line)
    return lines

# Constructor
class State():
    def __init__(self, name: str) -> None:
        """State init method

        Args:
            name (str): Name of state
        """
        self._name = name # State name

    def __repr__(self) -> str:
        return f"State(name='{self._name}')"

    def update(self, chapter_object: ChapterType, state: str) -> Optional[str]:
        """Updates a state class, and runs the code if
           if matches the name of the state

        Args:
            chapter_object (object): Chapter object
            state (str): New state name

        Returns:
            Optional[str]: Returns string if success, or error while calling
        """
        if state == self._name:
            # Checks if has the function "fire"
            method_to_call = getattr(self, "fire", None)
            if callable(method_to_call):
                method_to_call(chapter_object)
                return "Callable"
            else:
                return "Not callable"

def attachStates(chapter_object: ChapterType) -> None:
    """Attaches all states to a chapter object

    Args:
        chapter_object (object): Chapter object
    """
    for state in ready_states:
        chapter_object.attach(state)

# Event Methods
def onReadyFire(chapter_object: ChapterType) -> None:
    """Code runs when state is "Ready"

    Args:
        chapter_object (chapter.Chapter)
    """
    print("ready fired")

def onPreparingFire(chapter_object: ChapterType):
    """Code runs when state is "Preparing"

    Args:
        chapter_object (chapter.Chapter)
    """
    print("preparing fired")

    raw = chapter_object._raw
    lines = getLines(raw)
    chapter_object.lines = lines

    print("getting to here")

    # TODO: Calculations for stats
    chapter_object.stats = {
        "line_count": len(lines),
        "word_count": sum(len(line.split()) for line in lines)
    }

    chapter_object.setState("Ready")

# State Objects
preparing_object = newState("Preparing") # Preparing
ready_object = newState("Ready") # Ready

# Add new Attributes
def SetAttributes():
    setattr(preparing_object, "fire", onPreparingFire) # Preaparing
    setattr(ready_object, "fire", onReadyFire) # Ready

SetAttributes()