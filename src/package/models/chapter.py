print("Chapter Loaded")

import utils
import states

AVAILABLE_ID = 0

# Private Methods
def GetAvailableId() -> int:
    global AVAILABLE_ID
    AVAILABLE_ID = AVAILABLE_ID + 1
    return AVAILABLE_ID

# Constructor
class Chapter():
    def __init__(self, name: str, raw: str, book: str) -> None:
        """Object init method

        Args:
            name (str): Name of chapter
            raw (str): Raw string of chapter
            book (str): Assosicated book
        """
        # ID
        self._id = GetAvailableId() # Incase I need todo equality overrides
        self._title = name

        # Contents TODO: Literally haven't done any of this
        # Even though its like the most important part
        self._raw = raw # Only added if needed
        self.book = "" # Overall book the chapter is in
        self.lines = [] # Line objects or multidimensional

        # State 
        self._state = "Initializing" # Initializing, Content, Preparing, Ready
        self._observers = []
        self.initializing()

    @property
    def state(self) -> str:
        """Gets the current state of the chapter

        Returns:
            str: State name
        """
        return self._state
    
    def setstate(self, state: str) -> str:
        """Sets the current state to a new state

        Args:
            state (str): New state name

        Returns:
            str: Updated state name
        """
        self._state = state
        self.event() # Updates all states
        return self._state

    def attach(self, observer: object) -> None:
        """Attachs a new state observer

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

    def initializing(self) -> None:
        """Initializes chapter object logic
        """

        # Temporary fix till I figure out why its duplicated
        # Like what and why
        utils.remove_duplications(states.ready_states) 
        print(states.ready_states)
        # Assign all states as observers
        for state in states.ready_states:
            self.attach(state)
        
        self.setstate("Content")