from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Return True if ransomNote can be constructed from characters in magazine.

        Count characters in magazine and ensure ransomNote characters do not
        exceed available counts.
        """
        if not ransomNote:
            return True
        mag_counts = Counter(magazine)
        for ch in ransomNote:
            if mag_counts[ch] <= 0:
                return False
            mag_counts[ch] -= 1
        return True
