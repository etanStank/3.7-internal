from dataclasses import dataclass

# Data structures

@dataclass
class case:
    scenario: str
    file_name: str
    expect_error: bool

# Test cases

file_cases = [
    case("Valid chapter file", "lotmTest.txt", False), # Temporary case
    case("Valid chapter file", "valid.txt", False),
    case("Multiple files present (one target)", "multi_1.txt", False),
    case("Empty file", "empty.txt", False),
    case("File with blank lines", "blank_lines.txt", False),
    case("Unicode content", "unicode.txt", False),
    case("Very long file", "long.txt", False),
    case("Trailing newline", "trail_newline.txt", False),
    case("Tabs in content", "tabs.txt", False),
    case("Non-existent file", "missing.txt", True),
]

option_inputs = [
    case("Valid Option 1 by number", "1", False),
    case("Valid Option 1 by text", "read full chapter", False),

    case("Valid Option 2 by number", "2", False),
    case("Valid Option 2 by text", "read chapter by lines", False),

    case("Valid Option 3 by number", "3", False),
    case("Valid Option 3 by text", "show registered chapters", False),

    case("Valid Option 4 by number", "4", False),
    case("Valid Option 4 by text", "get stats of chapter", False),

    case("Valid Option 5 by number", "5", False),
    case("Valid Option 5 by text", "exit demo", False),

    case("Invalid Option by large number", "999" * 200, True),
    case("Invalid Option by small number", "999" * -200, True),
    case("Invalid Option by large text", "asd" * 250, True),
    case("Invalid Option by small text", "a", True)
]