from os import path
from pathlib import Path

import chapter


# Methods

def get_file_content(file):
    try:
        return file.read()
    except Exception as e:
        raise ValueError(f"Error while reading file: {e}")
    
def process_files(folder_path: str):
    print("Processing files...")
    folder = Path(folder_path)
    files = list(folder.glob("*.txt"))
    print(f"Found {len(files)} files")
    for file in files:
        print(f"Loading chapter: {file.name}")
        raw = file.read_text()
        chapter.Chapter(file.name, raw, "Unknown")

def init() -> None:
    base_dir = Path(__file__).parent
    process_files(str(base_dir / "test"))

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