from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Return the index of the first non-repeating character in s, or -1.

        Count character frequencies then scan for the first char with count 1.
        Time: O(n), Space: O(1) (character-count bounded by alphabet size).
        """
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
