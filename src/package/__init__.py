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
import chapter
import reader

"""

    DEMO INPUT MAPS

    1. Read full chapter
    2. Read chapter by lines
    3. Show registered chapters
    4. Get stats of chapter
    5. Exit demo


"""

def new_start():
    print("Starting Package")
    reader.init(DEMO, DEBUGGING)

    # if they want to repeat
    repeat = True

    if DEMO:
        # if demo is on, starts demo loop
        while repeat:
            # i promise i tried my hardest to make this look nice
            # i hate long strings i hate inputs
            # and this is both combined
            repeat = False
            print(f"Registered chapters: {chapter.REGISTERED_CHAPTERS}")
            print(f"\n\nWelcome to the demo! This is a terminal-based demonstration of the package's functionality. It processes chapter files and demonstrates state changes. Please check the output for details on the processing of each chapter and their states.")

            # holy text

            option_input = input(
            "What type of functionality would you like to see? (type 'exit' to quit)\n\n"
            "Options:\n"
            "1. Read full chapter\n"
            "2. Read chapter by lines\n"
            "3. Show registered chapters\n"
            "4. Get stats of chapter\n"
            "5. Exit demo\n\n"
            ).strip().lower()

            # Option 1: Read full chapter
            if option_input in ["1", "read full chapter"]:
                chapter_title = input("Enter the title of the chapter you want to read: ").strip().lower()
                chapter_object = chapter.GetChapterByName(chapter_title)
                if chapter_object:
                    print(f"-" * 20)
                    print(f"Name: {chapter_object._title},\nState: {chapter_object._state}\n\n")
                    for line in chapter_object.lines:
                        print(f"{line}\n\n")
                else:
                    print(f"Chapter with title '{chapter_title}' not found.")

            # Option 2: Read chapter by lines
            elif option_input in ["2", "read chapter by lines"]:
                chapter_title = input("Enter the title of the chapter you want to read: ").strip().lower()
                chapter_object = chapter.GetChapterByName(chapter_title)
                viewing = True
                if chapter_object:
                    print(f"-" * 20)
                    print(f"Name: {chapter_object._title},\nState: {chapter_object._state}\n\n")
                    while viewing:
                        line_input = input("Type 'next' to view the next line, or 'exit' to stop viewing: ").strip().lower()
                        if line_input == "next":
                            if chapter_object.lines:
                                print(chapter_object.lines[0])
                                chapter_object.lines.pop(0)
                            else:
                                print("No more lines to view.")
                                viewing = False
                        elif line_input == "exit":
                            viewing = False
                else:
                    print(f"Chapter with title '{chapter_title}' not found.")
            
            # Option 3: Show registered chapters
            elif option_input in ["3", "show registered chapters"]:
                print("Registered Chapters:")
                for chapter_object in chapter.REGISTERED_CHAPTERS:
                    print(f"- {chapter_object._title} (State: {chapter_object._state})")

            # Option 4: Get stats of chapter
            elif option_input in ["4", "get stats of chapter"]:
                chapter_title = input("Enter the title of the chapter you want to get stats of: ").strip().lower()
                chapter_object = chapter.GetChapterByName(chapter_title)
                if chapter_object:
                    print(f"Stats for Chapter '{chapter_object._title}':")
                    for stat_key, stat_value in chapter_object.stats.items():
                        print(f"- {stat_key}: {stat_value}")
                else:
                    print(f"Chapter with title '{chapter_title}' not found.")

            # Option 5: Exit demo
            elif option_input in ["5", "exit demo"]:
                print("Exiting demo. Goodbye")
                break
            
            # Repeat option
            again = input("\nDo you want to do something else? (y/n): ").strip().lower()
            if again in ["y", "yes"]:
                repeat = True
            elif again not in ["y", "yes"]:
                repeat = False
                print("Goodbye")
new_start()