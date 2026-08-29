LC-26: Remove Duplicates from Sorted Array

Approach:
- Two-pointer technique: maintain a write index for the next unique value.
- Iterate over the array with a read pointer; when current value differs from previous,
  write it at the write index and increment write.
- Return write as the new length; first `write` elements are the unique values.

Time complexity: O(n)
Space complexity: O(1)
