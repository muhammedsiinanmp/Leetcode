LC-27: Remove Element

Approach:
- Use two pointers: one for the next write position and one for scanning the array.
- When a value differs from val, copy it into the write position and advance the pointer.
- After the loop, the first `k` elements contain the remaining valid values.

Time complexity: O(n)
Space complexity: O(1)
