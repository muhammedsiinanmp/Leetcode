"""
242. Valid Anagram
Check whether two strings are anagrams using character counts.

Time complexity: O(n)
Space complexity: O(k), where k is the number of distinct characters
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = Counter()
        for ch in s:
            counts[ch] += 1

        for ch in t:
            if counts[ch] == 0:
                return False
            counts[ch] -= 1

        return all(v == 0 for v in counts.values())


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aacc", "ccaa", True),
        ("", "", True),
    ]
    for s, t, expected in samples:
        print(f"{s}, {t} -> {sol.isAnagram(s, t)} (expected {expected})")
