from dataclasses import dataclass

# Data structures

@dataclass
class case:
    scenario: str
    file_name: str
    expect_error: bool

# Test cases

cases = [
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