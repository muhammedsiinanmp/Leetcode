import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_3_module",
    os.path.join(os.path.dirname(__file__), "..", "strings", "LC_3.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_length_of_longest_substring():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("dvdf") == 3


if __name__ == "__main__":
    test_length_of_longest_substring()
    print("All tests passed for LC3")
