LC-35: Search Insert Position

Approach:
- Use binary search on the sorted array.
- Keep track of the left and right bounds, shrinking toward the first index where
  nums[mid] >= target.
- If target is not found, return the insertion point `left`.

Time complexity: O(log n)
Space complexity: O(1)
