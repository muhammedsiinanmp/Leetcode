class Solution:
    def reverseString(self, s: list[str]) -> None:
        """Reverse the list of characters in-place using two pointers."""
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        # function modifies in place; return None explicitly
        return None
