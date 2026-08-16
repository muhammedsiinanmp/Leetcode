"""
242. Valid Anagram
Check whether two strings are anagrams using character counts.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = Counter(s)

        for ch in t:
            # if a character is missing or overused, the strings are not anagrams
            if counts[ch] == 0:
                return False
            counts[ch] -= 1

        # all characters must be matched exactly once
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
