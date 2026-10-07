LC 189 - Rotate Array

Problem: Given an integer array nums, rotate the array to the right by k
steps, modifying it in place (no value may be returned).

Approach:
- Reduce k with `k %= n`. Rotating by n steps is a full lap, so only the
  remainder matters; without this a k larger than the list would do
  pointless work, and k >= n would break index arithmetic.
- The classic three-reverse trick:
  - reverse the whole array
  - reverse the first k elements
  - reverse the remaining n - k elements
- Reversing everything first puts the last k elements at the front, but in
  reversed order; the two follow-up reverses restore each block's original
  order while keeping their swapped positions.
- The reversal helper swaps with a two-pointer walk, so the whole rotation
  stays in the caller's list: LeetCode inspects `nums` directly and the
  function must return None.

Time complexity: O(n) - every element is touched a constant number of times.
Space complexity: O(1) extra space; only three integers of bookkeeping.
