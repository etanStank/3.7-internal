"""Module for loading and processing chapter text files for demo or testing."""

from pathlib import Path

from test import cases
import chapter

# Easy management of datapath for files
DATAPATH = Path(__file__).parent / "data"

# Updated through the __init__.py file
DEBUGGING = False

# Updated through the __init__.py file
DEMO = False


def get_file_content(file: Path) -> str:
    """Read and return the content of a file.

    This method allows for the content of a file
    to be read and returned as a string, while handling
    any errors that occur.

    Args:
        file (Path): The file to read.

    Returns:
        str: The content of the file as a string.
    """
    try:
        # Trys to read the files content, and raises an error if it fails.
        return file.read_text()
    except Exception as e:
        # Error is raised when file's content cannot be read.
        raise ValueError(f"Error while reading file: {e}")


def process_files(folder_path: str) -> None:
    """Process all .txt files in the given folder.

    This method allows for the file to be processed,
    and initailizes a chapter object.

    Args:
        folder_path (Path): Typically DATAPATH, unless testing
    """
    # Gets the folder from the path using pathlib
    folder = Path(folder_path)

    # Gets any files in the folder that are .txt's
    files = list(folder.glob("*.txt"))

    for file in files:
        # Loops through all the files,
        # Gets the raw content of the file
        raw = get_file_content(file)

        # Temporarily puts the name as 'Unknown'
        # Till it can be properly identified
        book_name = "Unknown"

        # Creates the chapter object using the file data
        chapter.Chapter(file.name, raw, book_name)


def init(demo: bool, debugging: bool) -> None:
    """Initialize the program in demo or debugging mode.

    This method allows for the program to properly run, in
    either the demo, or debugging mode. Alongside properly
    regulating how the demo / debugging mode is used. This
    allows for easy debugging, and displaying the demo, alongside
    removing the demo.

    Args:
        demo (Bool): If demo is being active
        debugging (Bool): If debugging is active
    """
    # Gets global DEBUGGING, DEMO
    global DEBUGGING, DEMO
    DEBUGGING = debugging
    DEMO = demo

    if not DEBUGGING and DEMO:
        # Runs if only the DEMO is active
        process_files(str(DATAPATH))

    elif DEBUGGING and DEMO:
        # Raises an error if both the debugging
        # and demo is active, as the debugging files
        # don't contain any useful data to be presented.
        raise ValueError(
            "Cannot run in both demo and debugging mode at the same time."
        )

    if DEBUGGING and not DEMO:
        # Runs only if DEBUGGING is active
        print("Preparing test cases")

        for case in cases.cases:
            # Loops through all test cases in cases.py
            print(f"Testing case: {case.scenario}")

            # Attempts the case
            try:
                # Gets the file based on the case.file_name, and in
                # the 'test' folder
                file_path = (
                    Path(__file__).parent / "test" / case.file_name
                )

                # Trys to get the raw content of it
                raw = get_file_content(file_path)

                # Attempts to create a chapter object using the data
                # found, and puts it in the 'Testing' book, for easy
                # mangement (unless testing in multiple books)
                chapter.Chapter(
                    case.file_name,
                    raw,
                    "Testing"
                )

                if case.expect_error:
                    # Runs if there is an expected error,
                    # but none was raised / happened.
                    print(
                        f"🟠 Case '{case.scenario}' expected an error "
                        "but none occurred."
                    )
                else:
                    # Runns if there was no expected error,
                    # and if there was no error raised
                    print(
                        f"🟢 Case '{case.scenario}' passed without error."
                    )

            except Exception as e:
                if not case.expect_error:
                    # Runs if there was no expected error,
                    # but one / multiple were raised.
                    print(
                        f"🔴 Unexpected error for case "
                        f"'{case.scenario}': {e}"
                    )
