class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of needle in haystack, or -1.

        Uses a simple sliding window (Python slicing). For long strings a KMP
        implementation would be better, but slicing is concise and correct for tests.
        """
        if needle == "":
            return 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
