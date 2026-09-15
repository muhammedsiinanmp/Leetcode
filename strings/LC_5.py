class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return the longest palindromic substring using center expansion."""
        if len(s) < 2:
            return s

        start = end = 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for center in range(len(s)):
            odd_start, odd_end = expand(center, center)
            even_start, even_end = expand(center, center + 1)
            if odd_end - odd_start > end - start:
                start, end = odd_start, odd_end
            if even_end - even_start > end - start:
                start, end = even_start, even_end

        return s[start:end + 1]
