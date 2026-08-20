class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Return the length of the last word in a trimmed string.

        Strategy: strip trailing/leading spaces and split on spaces; the last
        token is the final word, whose length is the answer.
        """
        words = s.strip().split()
        return len(words[-1]) if words else 0
