LC 283 - Move Zeroes

Problem: Given an integer array nums, move all 0's to the end while keeping
the relative order of the non-zero elements, modifying the array in place
(no value may be returned).

Approach:
- Keep a slow `write` index that marks the next slot for a non-zero value.
- Walk the array once with a read loop. Whenever a non-zero element shows
  up, copy it into nums[write] and advance write.
- Copying instead of swapping is safe here: the read pointer is always at
  or ahead of the write pointer, so a slot is never overwritten before its
  value has been read. That keeps the relative order of non-zero elements
  exactly as it was.
- After the walk, every index from `write` to the end still holds a stale
  value, so overwrite that tail with zeroes.
- The whole thing stays in the caller's list: LeetCode inspects `nums`
  directly and the method must return None.

Time complexity: O(n) - one pass to compact plus one pass to fill the tail.
Space complexity: O(1) extra space; only the write index is tracked.
