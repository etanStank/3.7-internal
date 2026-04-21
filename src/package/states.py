"""

TODO: Fix duplication, like why. Could add
      equality override worst case scenario
      Why do I always overcomplicate stuff.
"""


print("States Loaded")

from typing import Optional

import chapter

ready_states = []

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
        ready_states.append(self) # Accessibility

    def __repr__(self) -> str:
        return f"State(name='{self._name}')"

    def update(self, chapter_object: object, state: str) -> Optional[str]:
        """Updates a state class, and runs the code if
           if matches the name of the state

        Args:
            chapter_object (object): Chapter object
            state (str): New state name

        Returns:
            Optional[str]: Returns string if success, or error while calling
        """
        if state == self._name:
            print(f"Checking {state} with object {self._name}")
            # Checks if has the function "fire"
            method_to_call = getattr(self, "fire", None)
            if callable(method_to_call):
                print("Callable")
                method_to_call(chapter_object)
                return "Callable"
            else:
                print("Not callable")
                return "Not callable"


# Event Methods
def onReadyFire(chapter_object: chapter.Chapter) -> None:
    """Code runs when state is "Ready"

    Args:
        chapter_object (chapter.Chapter)
    """
    print(chapter_object.stats)
    print(f"Line count; {chapter_object.getStat('line_count')}")
    print(f"Word count; {chapter_object.getStat('word_count')}")
    print("ready fired")

def onContentFire(chapter_object: chapter.Chapter) -> None:
    """Code runs when state is "Content"

    Args:
        chapter_object (chapter.Chapter)
    """
    print("content fired")

def onPreparingFire(chapter_object: chapter.Chapter):
    """Code runs when state is "Preparing"

    Args:
        chapter_object (chapter.Chapter)
    """
    print("preparing fired")

    raw = chapter_object._raw
    lines = getLines(raw)
    chapter_object.lines = lines

    # TODO: Calculations for stats
    chapter_object.stats = {
        "line_count": len(lines),
        "word_count": sum(len(line.split()) for line in lines)
    }

    chapter_object.setstate("Ready")

# Content Objects
content_object = State("Content") # Content
ready_states.append(content_object)

preparing_object = State("Preparing") # Preparing
ready_states.append(preparing_object)

ready_object = State("Ready") # Ready
ready_states.append(ready_object)


# Add new Attributes
setattr(content_object, "fire", onContentFire) # Content
setattr(preparing_object, "fire", onPreparingFire) # Preaparing
setattr(ready_object, "fire", onReadyFire) # Ready
