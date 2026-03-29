from pathlib import Path

print("be,l")

folder_path = Path('../data/raws') # Create a Path object
# Use .glob() for non-recursive search in the current folder, .rglob() for subdirectories

for file_path in folder_path.glob("*.txt"):
    print(file_path)
    print("hi")
    # read_text() is a convenient method that handles opening, reading, and closing
    content = file_path.read_text(encoding='utf-8') 
    print(f"--- Content of {file_path.name} ---")
    print(content)
    print("-" * 30)

