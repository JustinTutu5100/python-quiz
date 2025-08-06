
# Define a function that identifies the first non-repeating character in a given string.
# The comparison is case-insensitive, but the original casing of the character is preserved in the output.
# If all characters repeat, the function returns an empty string.

def first_non_repeated(s: str) -> str:
    """
    Returns the first non-repeating character in the string s.
    Comparison is case-insensitive, but returns the original case.
    """
    lower = s.lower()
    for idx, ch in enumerate(lower):
        if lower.count(ch) == 1:
            return s[idx]
    return ""

