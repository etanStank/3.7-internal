from multiprocessing import Value
from os import path
from pathlib import Path
from re import DEBUG

from test import cases
import chapter

DATAPATH = Path(__file__).parent / "data" 

DEBUGGING = False
DEMO = False

# Methods

def get_file_content(file):
    try:
        return file.read_text()
    except Exception as e:
        raise ValueError(f"Error while reading file: {e}")
    
def process_files(folder_path: str):
    print("Processing files...")
    folder = Path(folder_path)
    files = list(folder.glob("*.txt"))
    print(f"Found {len(files)} files")
    for file in files:
        print(f"Loading chapter: {file.name}")
        raw = get_file_content(file)
        bookName = "Unknown"
        print(file.name)
        chapter.Chapter(file.name, raw, bookName)

def init(demo: bool, debugging: bool) -> None:
    global DEBUGGING, DEMO
    DEBUGGING = debugging
    DEMO = demo

    if not DEBUGGING and DEMO:
        process_files(str(DATAPATH))
    elif DEBUGGING and DEMO:
        raise ValueError("Cannot run in both demo and debugging mode at the same time.")
    if DEBUGGING and not DEMO:
        print("Preparing test cases")
        for case in cases.cases:
            print(f"Testing case: {case.scenario}")
            try:
                file_path = Path(__file__).parent / "test" / case.file_name
                raw = get_file_content(file_path)
                chapter.Chapter(case.file_name, raw, "Testing")
                if case.expect_error:
                    print(f"🟠 Case; '{case.scenario}' expected an error but none occurred.")
                elif not case.expect_error:
                    print(f"🟢 Case; '{case.scenario}' passed without error.")
            except Exception as e:
                if not case.expect_error:
                    print(f"🔴 Unexpected error for case '{case.scenario}': {e}")

'''def process_files(folder_path: str):
    print("Processing files...")
    folder = Path(folder_path)
    files = list(folder.glob("*.txt"))
    for file in files:
        print(f"Loading chapter; {file.name}")
        print(file)
        raw = get_file_content(file)
        print(raw)
        #chapter_object = chapter.Chapter(file.name, raw, "Unknown")

def init() -> None:
    print("Initialization of Reader complete.")
    process_files("test/")'''