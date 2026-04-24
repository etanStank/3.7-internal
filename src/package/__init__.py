"""

My temporary testing file, I really need to get the test cases file working..
Too early to deal with edge cases.

TODO: 
    - Method to export it?
    - terminal demo
    - test cases half done, need more
"""
DEBUGGING = False
DEMO = True

from sre_parse import REPEAT_CHARS
import time

import chapter
import reader
import states

REPEAT = 1

#chapter1 = chapter.Chapter("Chapter1", "asd", "Book1")

#print(chapter1.state)
#chapter1.setstate("Preparing")

def standard_start():
    print("Starting Package")
    reader.init(DEMO, DEBUGGING)

    if DEMO:
        global REPEAT
        print(f"Current Loop: {str(REPEAT)}")
        REPEAT = REPEAT + 1
        print("Starting demo")
        reader.init(DEMO, DEBUGGING)
        print(f"Registered chapters: {chapter.REGISTERED_CHAPTERS}")
        print(f"\n\nWelcome to the demo! This is a terminal-based demonstration of the package's functionality. It processes chapter files and demonstrates state changes. Please check the output for details on the processing of each chapter and their states.")
        function_input = input("What type of functionality would you like to see? (type 'exit' to quit)\n\nOptions:\n1. Process chapter files\n2. Show registered chapters\n3. Show states of chapters\n\n4. Read a chapter")
        function_input = function_input.strip().lower()
        if function_input == "exit":
            print("Exiting demo. Thank you for trying it out!")
        elif function_input == "2" or function_input == "show registered chapters":
            print(chapter.REGISTERED_CHAPTERS)
            for chapter_object in chapter.REGISTERED_CHAPTERS:
                print(f"-" * 20)
                print(f"Name: {chapter_object._title},\nBook: {chapter_object.book._name}\nState: {chapter_object._state}\n\n")
                for stat in chapter_object.stats:
                    print(f"{stat}: {chapter_object.stats[stat]}")
        elif function_input == "3" or function_input == "show states of chapters":
            for chapter_object in chapter.REGISTERED_CHAPTERS:
                print(f"Chapter: {chapter_object._title}, States: {chapter_object._state}")
        elif function_input == "4" or function_input == "read a chapter":
            chapter_title = input("Enter the title of the chapter you want to read: ")
            chapter_title = chapter_title.strip()
            chapter_object = next((ch for ch in chapter.REGISTERED_CHAPTERS if ch._title == chapter_title), None)
            if chapter_object:
                print(f"-" * 20)
                print(f"Name: {chapter_object._title},\nBook: {chapter_object.book._name}\nState: {chapter_object._state}\n\n")
                for line in chapter_object.lines:
                    print(line)
            else:
                print(f"Chapter with title '{chapter_title}' not found.")

standard_start()