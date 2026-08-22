LC-14: Longest Common Prefix

Approach:
- Use the first string as an initial prefix and iteratively shorten it while
  it is not a prefix of each following string (horizontal scanning).
- Early exit when prefix becomes empty.

Time complexity: O(S) where S is the sum of all characters in the input array.
Space complexity: O(1) extra space.
