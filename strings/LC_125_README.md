LC-125: Valid Palindrome

Approach:
- Use two pointers (i, j) starting at string ends.
- Skip non-alphanumeric characters using str.isalnum().
- Compare lowercase characters; if mismatch, return False.
- Otherwise advance pointers and continue until i >= j.

Time complexity: O(n)
Space complexity: O(1) (ignoring input storage)
