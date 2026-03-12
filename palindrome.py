import re

def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignore non-alphanumerics and case)."""
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    tests = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "No 'x' in Nixon",
    ]
    for t in tests:
        print(f"{t!r} -> {is_palindrome(t)}")
