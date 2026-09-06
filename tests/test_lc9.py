import importlib.util
import os

# Import the solution by file path to avoid conflicting with stdlib 'math' module
spec = importlib.util.spec_from_file_location(
    "LC_9_module",
    os.path.join(os.path.dirname(__file__), '..', 'math', 'LC_9.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_is_palindrome():
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False  # negative numbers are not palindrome
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(0) is True
    assert s.isPalindrome(123454321) is True


if __name__ == "__main__":
    test_is_palindrome()
    print("All tests passed for LC9")
