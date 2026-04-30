"""Acts as a demo and testing ground for the package."""

import chapter
import reader

# Easy management of demo, and debugging modes
# allowing for easy switching between the two modes
# Debugging mode allows for testing using the cases.py file
DEBUGGING = False

# Demo mode allows for the __init__.py file to run a
# terminal-based demo of the package.
DEMO = True


def start():
    """Start the demo loop and handle user interaction.

    This method acts as the start for either the demo,
    or debugging.
    """
    print("Starting Package")

    # Initializes the reader, which goes
    # through the files
    reader.init(DEMO, DEBUGGING)

    # Used so the user can repeat options menu
    repeat = True

    if DEMO:
        # If demo is being ran
        while repeat:
            # While user is repeating
            repeat = False

            # -------------------------
            # Information Section
            # -------------------------

            # Details on the demo
            print(
                "\n\nWelcome to the demo! This is a terminal-based "
                "demonstration of the package's functionality. It processes "
                "chapter files and demonstrates state changes. Please check "
                "the output for details on the processing of each chapter "
                "and their states."
            )

            # Option input
            option_input = input(
                "What type of functionality would you like to see? "
                "(type 'exit' to quit)\n\n"
                "Options:\n"
                "1. Read full chapter\n"
                "2. Read chapter by lines\n"
                "3. Show registered chapters\n"
                "4. Get stats of chapter\n"
                "5. Exit demo\n\n"
            ).strip().lower()

            # Checks if the option_input is either 1, or read full chapter
            # allows for either or, to be more accessible
            if option_input in ["1", "read full chapter"]:
                # Checks what chapter they want to see,
                # through allowing them to input it
                chapter_title = input(
                    "Enter the title of the chapter you want to read: "
                ).strip().lower()

                # Gets the chapter using the chapter_title inputted
                chapter_object = chapter.get_chapter_by_name(
                    chapter_title
                )

                # Checks if the chapter_object exists
                if chapter_object:
                    # Allows for a seperator
                    print("-" * 20)

                    # Prints core chapter information
                    # could remove state more for debugging
                    print(
                        f"Name: {chapter_object._title},\n"
                        f"State: {chapter_object._state}\n\n"
                    )

                    # Prints all the lines in chapter_object
                    for line in chapter_object.lines:
                        print(f"{line}\n\n")

                # If the chapter_object doesn't exist
                else:
                    print(
                        f"Chapter with title '{chapter_title}' not found."
                    )

            # Checks if the option_input is either 2, or read chapter by lines
            # allows for either or, to be more accessible
            elif option_input in ["2", "read chapter by lines"]:
                # Checks what chapter they want to see,
                # through allowing them to input it
                chapter_title = input(
                    "Enter the title of the chapter you want to read: "
                ).strip().lower()

                # Gets the chapter using the chapter_title inputted
                chapter_object = chapter.get_chapter_by_name(
                    chapter_title
                )

                # Boolean to check if they still want to view
                # the chapter
                viewing = True

                if chapter_object:
                    # Allows for a seperator for previosu content
                    print("-" * 20)

                    # Prints core chapter information
                    # could remove state more for debugging
                    print(
                        f"Name: {chapter_object._title},\n"
                        f"State: {chapter_object._state}\n\n"
                    )

                    # While they are viewing the chapter
                    while viewing:
                        # Gets if they want the next line, or to exit
                        # strips, and lowers it for easy checking
                        line_input = input(
                            "Type 'next' to view the next line, or "
                            "'exit' to stop viewing: "
                        ).strip().lower()

                        # If they want to go to the next line
                        if line_input == "next":
                            if chapter_object.lines:
                                # Prints the line
                                print(chapter_object.lines[0])
                                chapter_object.lines.pop(0)
                            else:
                                # Tells the user there are no more
                                # lines
                                print("No more lines to view.")
                                viewing = False
                        # If they want to exit
                        elif line_input == "exit":
                            # Stops the loop
                            viewing = False
                else:
                    print(
                        f"Chapter with title '{chapter_title}' not found."
                    )

            # Checks if the option_input is either 3, or show registered chapters
            # allows for either or, to be more accessible
            elif option_input in ["3", "show registered chapters"]:
                # Prints out all the chapters in REGIISTER_CHAPTERS
                print("Registered Chapters:")
                for chapter_object in chapter.REGISTERED_CHAPTERS:
                    # Loops through the chapter objects, and prints
                    # the title, and state
                    print(
                        f"- {chapter_object._title} "
                        f"(State: {chapter_object._state})"
                    )

            # Checks if the option_input is either 4, get stats of chapter
            # allows for either or, to be more accessible
            elif option_input in ["4", "get stats of chapter"]:
                # Checks what chapter they want to see,
                # through allowing them to input it,
                # strips, and lowers it for easy checking
                chapter_title = input(
                    "Enter the title of the chapter you want to get stats of: "
                ).strip().lower()

                # Gets the chapter_object by using the chapter_title inputted
                chapter_object = chapter.get_chapter_by_name(
                    chapter_title
                )

                # Checks if the chapter_object exists
                if chapter_object:
                    # Prints out the stats for the chapter object
                    print(
                        f"Stats for Chapter '{chapter_object._title}':"
                    )
                    for stat_key, stat_value in chapter_object.stats.items():
                        # Loops through the stats in the .stats dictionary
                        # As its a dictionary its able to print the key
                        # eg, line_count alongside its value easily
                        print(f"- {stat_key}: {stat_value}")
                else:
                    print(
                        # If the desired chapter cannot be found
                        f"Chapter with title '{chapter_title}' not found."
                    )

            # Checks if the option_input is either 5, exit demo
            # allows for either or, to be more accessible
            elif option_input in ["5", "exit demo"]:
                # Exits you out of the demo
                print("Exiting demo. Goodbye")
                break

            # Checks if you want to use the terminal again after
            # compeleting whatever function you originally wanted
            # strips, and lowers (makes it lowercase) the text for
            # easy checking
            again = input(
                "\nDo you want to do something else? (y/n): "
            ).strip().lower()

            # if they want to do something else / try again
            # they can include y, or yes in their message
            if again in ["y", "yes"]:
                repeat = True
            # if they don't include y, or yes in the message
            # it exits them from the demo
            else:
                repeat = False
                print("Goodbye")


start()
