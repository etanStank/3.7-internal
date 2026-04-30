"""Manage state objects and their interaction with chapters.

This code relies on an Observer Pattern, which allows for the
chapter to run specific code based on what state this is in. I
chose this method as when creating these chapters, it is very
instructional if thats the wording (Step 1, Step 2, etc). The
Observer Pattern allows for this to be done very easy as each step
is grouped by a state such as Initializing, Preparing, or Ready. Which
has sub steps that need to be completed before finishing the grater step,
allowing for the chapter object to follow each step properly to ensure that
the two files can communicate to each other easily, while also being in sync.
Also cause I thought it would be cool to try out.
"""

from typing import Optional

# Allows for easy retrieval of state objects by name,
# and management of ready states. This is used in specific
# for when the states are attached to each object.
READY_STATES = []

# Used as the state positions when using the chapter's
# next_state method.
STATE_POSITIONS = [
    "Initializing",
    "Preparing",
    "Ready",
]

# -------------------------
# Public Methods
# -------------------------


def new_state(name: str) -> Optional["State"]:
    """Create and register a new state object.

    This method allows for the creation fo a new
    state, while ensuring that it does not already
    exist in READY_STATES, preventing duplication.

    Args:
        name (str): Name of the new state

    Returns:
        Optional[State]: State if created, otherwise None
    """
    # Duplicate Prevention
    for state in READY_STATES:
        # Loops through all states in READY_STATES, and checks
        # if they are the same name as the current state being
        # created
        if state._name == name:
            raise ValueError(f"State with name '{name}' already exists.")

    # Creates the new state, and appends it to READY_STATE
    state_obj = State(name)
    READY_STATES.append(state_obj)
    return state_obj


def attach_states(chapter_object) -> None:
    """Attach all registered states to a chapter.

    This method allows for the attachment of
    all states in READY_STATES to a specific chapter.
    Allows for easy customization of the process in
    the future if required.

    Args:
        chapter_object (chapter): Chapter object
    """
    for state in READY_STATES:
        # Loops through all states in READY_STATES
        # Attachs them using the .attach method
        chapter_object.attach(state)


# -------------------------
# Private Helpers
# -------------------------


def get_lines(raw: str) -> list:
    """Split raw text into cleaned, non-empty lines.

    This method allows for the raw content of the chapter
    to be split into lines, while handling any errors
    which could occur during the process.

    Args:
        raw (str): Chapter object's raw content

    Returns:
        list: Raw content seperated into a list by lines
    """
    if not raw:
        # Checks if there is any raw content
        # Returns an empty list as there is no content
        return []

    if "\n" not in raw:
        # Checks if there is multiple lines in the
        # raw content, otherwise just strips the contnet
        # and returns the raw content
        return [raw.strip()]

    # Holds all of the split lines
    lines = []

    for line in raw.split("\n"):
        # Loops through each line seperated by "\n"
        # Strips the line of any unnessecary spaces
        line = line.strip()

        # Sanity check to ensure the line exists
        # after stripping, then adds to lines
        if line:
            lines.append(line)

    return lines


# -------------------------
# State Class
# -------------------------
class State:
    """Represent a state in the chapter lifecycle.

    Each state has a unqiue name upon creation. As
    the more important part is the update method, which allows
    for the observer pattern to work. Could be seen as a "hack"
    approach.
    """

    def __init__(self, name: str) -> None:
        """Initialize the state.

        Args:
            name (str): Name of the state
        """
        self._name = name

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the state.

        This method provides a clear and concise
        representation of the state object, useful for
        debugging purposes.

        Returns:
            str: A string representation of the state object.
        """
        return f"State(name='{self._name}')"

    # -------------------------
    # State Handler
    # -------------------------
    def update(self, chapter_object, state: str) -> Optional[str]:
        """Fire the state's handler if names match.

        This method allows for the state to update itself,
        this allows the associated method such as on_preparing_fired
        to be fired, thus allowing for the greater observer pattern
        to work.

        Args:
            chapter_object (chapter): Chapter object to update
            state (str): Name of the new state

        Returns:
            Optional[str]: If callable, or not callable
        """
        # Checks if the state equals the state name
        # As this method is ran on all states
        if state == self._name:
            # Gets the corrosponding fire method
            method = getattr(self, "fire", None)

            # Sanity check on the method found
            # Checking if it is callable (aka a method)
            if callable(method):
                # Runs the method
                method(chapter_object)
                return "Callable"

            return "Not callable"

        return None


# -------------------------
# State Firing Methods
# -------------------------
def on_ready_fire(chapter_object) -> None:
    """Run when state is 'Ready'.

    This method is ran when the chapter object
    is in the "Ready" state. And contains all 'sub-steps'
    in the method here, allowing for easy management.

    Args:
        chapter_object (chapter): Chapter object
    """
    # Empty... Can be removed later on, I guess.
    print("ready fired")


def on_preparing_fire(chapter_object) -> None:
    """Run when state is 'Preparing'.

    This method is ran when the chapter object
    is in the "Preparing" state. And contains all 'sub-steps'
    in the method here, allowing for easy management.

    Args:
        chapter_object (chapter): Chapter object
    """
    print("preparing fired")

    # Gets all of the lines using get_lines from the
    # chapter_object's raw content, and then adds it
    # to the chapter_objects lines attribute
    lines = get_lines(chapter_object._raw)
    chapter_object.lines = lines

    # Does the stats for the chapter_object
    chapter_object.stats = {
        # Gets the line count using len(lines), simple approach
        "line_count": len(lines),
        # Gets the word count by looping through each line
        # And splitting the line (by spaces) to get each word
        "word_count": sum(len(line.split()) for line in lines),
    }

    # Changes the chapter_objects state
    chapter_object.next_state()


# -------------------------
# State Initialization
# -------------------------

# Creates the new Preparing state object
preparing_state = new_state("Preparing")

# Creates the new Ready state object
ready_state = new_state("Ready")

# Sets the attribute of the preparing state, using
# the setattr method. Using the state object, then the
# method name (always "fire"), and then the method
# such as on_preparing_fire. This allows for dynamic
# additions.
setattr(preparing_state, "fire", on_preparing_fire)
setattr(ready_state, "fire", on_ready_fire)
