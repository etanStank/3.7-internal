"""

My temporary testing file, I really need to get the test cases file working..
Too early to deal with edge cases.

TODO: 
    - Method to export it?
    - terminal demo
"""

import chapter
import reader
import states

#chapter1 = chapter.Chapter("Chapter1", "asd", "Book1")

#print(chapter1.state)
#chapter1.setstate("Preparing")

for chapter_object in chapter.REGISTERED_CHAPTERS:
    print(chapter_object)
    for state in states.ready_states:
        chapter_object.attach(state)


reader.init()