"""

TODO: Fix duplication, like why. Could add
      equality override worst case scenario
      Why do I always overcomplicate stuff.
"""


print("States Loaded")

from typing import Optional

import chapter

ready_states = []

# Constructor
class State():
    def __init__(self, name: str) -> None:
        """State init method

        Args:
            name (str): Name of state
        """
        self._name = name # State name
        ready_states.append(self) # Accessibility

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

content_object = State("Content") # TODO: Organize this stuff better, like what. its annoying me.
ready_states.append(content_object)

def onContentFire(chapter_object: chapter.Chapter) -> None:
    """Code runs when state is "Content"

    Args:
        chapter_object (chapter.Chapter)
    """
    print("content fired")

preparing_object = State("Preparing") # TODO: what I said above.
ready_states.append(preparing_object)

def onPreparingFire(chapter_object: chapter.Chapter):
    """Code runs when state is "Preparing"

    Args:
        chapter_object (chapter.Chapter)
    """
    print("preparing fired")

# Assignment
setattr(content_object, "fire", onContentFire) # Content
setattr(preparing_object, "fire", onPreparingFire) # Preaparing
