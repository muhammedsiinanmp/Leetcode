class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring without repeated characters."""
        last_seen = {}
        window_start = 0
        longest = 0

        for index, character in enumerate(s):
            if character in last_seen and last_seen[character] >= window_start:
                window_start = last_seen[character] + 1
            last_seen[character] = index
            longest = max(longest, index - window_start + 1)

        return longest
