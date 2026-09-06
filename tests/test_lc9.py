from math.LC_9 import Solution


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
