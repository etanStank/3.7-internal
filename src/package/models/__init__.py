from random import setstate

import chapter

class State():
    def __init__(self, name) -> None:
        self._name = name

    def update(self, state):
        if state == self._name:
            print("state name active")

initialize = State("ASD123")
chapter1 = chapter.Chapter("Chapter1", "asd", "Book1")

chapter1.attach(initialize)
print(chapter1.state)
chapter1.setstate("ASD123")
print(chapter1.state)
chapter1.event()