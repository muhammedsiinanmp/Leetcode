LC 88 - Merge Sorted Array

Problem: Given two non-decreasing integer arrays, merge the second into the
first in non-decreasing order. The first array has enough trailing space to
hold all values, and the merge must happen in place.

Approach:
- Start at the end of each array and write the larger remaining value into the
  last available position in the first array.
- Continue until all values from the second array have been copied. Any values
  remaining in the first array are already in the correct positions.

Time complexity: O(m + n)
Space complexity: O(1) extra space
