import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_5_module",
    os.path.join(os.path.dirname(__file__), "..", "strings", "LC_5.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_longest_palindrome():
    solution = Solution()
    assert solution.longestPalindrome("babad") in {"bab", "aba"}
    assert solution.longestPalindrome("cbbd") == "bb"
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("") == ""
    assert solution.longestPalindrome("racecar") == "racecar"


if __name__ == "__main__":
    test_longest_palindrome()
    print("All tests passed for LC5")
