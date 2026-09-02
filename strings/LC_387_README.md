LC-387: First Unique Character in a String

Approach:
- Count character frequencies using collections.Counter.
- Scan the string left-to-right and return the index of the first character with count 1.

Time complexity: O(n)
Space complexity: O(1) (bounded alphabet)
