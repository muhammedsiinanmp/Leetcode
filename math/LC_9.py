class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Return True if integer x is a palindrome.

        Negative numbers are not palindromes. The simplest correct approach here
        is to convert to string and compare with its reverse. This is easy to
        read and fine for problem constraints.
        """
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
