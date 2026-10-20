LC 301 - Remove Duplicates from an Array

Problem: Given an integer array `nums` sorted in non-decreasing order, remove
the duplicates **in place** so that the first `k` entries hold the distinct
values and return `k`. Entries from index `k` onward are undefined and do not
need to be preserved.

Approach:
- Keep `k`, the length of the distinct prefix built so far. `nums[0]` is always
  a distinct value, so an empty array returns `0` and otherwise `k` starts at `1`.
- Scan from index `1` and compare each value against the last accepted one,
  `nums[k - 1]`. If they differ, copy the value to `nums[k]` and advance `k`.
- Because `k <= i` always, every write lands on an index that has already been
  read. No unread element is ever overwritten and no auxiliary buffer is needed.
- The sorted precondition is what makes this work: equal values are contiguous,
  so comparing against the single previous distinct value catches every
  duplicate. On unsorted input a hash set would be required instead.

Example: `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` becomes `[0, 1, 2, 3, 4, ...]` with
`k = 5`.

Time complexity: O(n) - one pass, each element compared once.
Space complexity: O(1) - compaction happens in the input array itself.