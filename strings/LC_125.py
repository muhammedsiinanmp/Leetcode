class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Return True if s is a palindrome after removing non-alphanumeric
        chars and ignoring case. Two-pointer approach in O(n) time and O(1) extra space.
        """
        i, j = 0, len(s) - 1
        while i < j:
            # move i forward to next alnum
            while i < j and not s[i].isalnum():
                i += 1
            # move j backward to prev alnum
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
