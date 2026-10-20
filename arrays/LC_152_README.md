LC 152 - Maximum Product Subarray

Problem: Given an integer array `nums`, return the largest product of any
**non-empty** contiguous subarray. `nums` always contains at least one element.

Approach:
- Kadane's algorithm works here, but one extra variable is needed compared to the
  sum version (LC-53). Track three values as the scan advances:
  - `cur_max`: the largest product of any subarray **ending at** the current index
  - `cur_min`: the smallest product of any subarray ending at the current index
  - `best`: the largest product of any subarray seen so far
- The subarray ending at `x` either starts fresh at `x` or extends a subarray
  ending at `x - 1`, so each candidate set is `{x, cur_max * x, cur_min * x}` and
  `best = max(best, cur_max)`.
- **Why `cur_min` is required.** Multiplying by a negative reverses ordering, so
  the subarray with the *smallest* ending product becomes the one with the
  *largest* product once a negative is applied. Tracking only `cur_max` discards
  exactly the candidate that later wins. On `[-2, 3, -4]` a max-only variant
  answers `3` (the `-2` is dropped for failing to beat it), while the correct
  answer is `24` from `[-2, 3, -4]`.
- **The swap.** Since a negative `x` is known in advance to reverse the order of
  the two products, `cur_max` and `cur_min` are exchanged up front and the two
  updates stay symmetric. This is equivalent to evaluating all three candidates
  but multiplies once instead of twice.
- Both are seeded from `nums[0]`, never from `0`. The subarray must be non-empty,
  so an all-negative input must report its least-negative single element rather
  than the empty product `0`.

Worked example, `[-2, 3, -4]`:

| x | cur_max | cur_min | best |
|---|---------|---------|------|
| -2 | -2 | -2 | -2 |
| 3  | 3 | -6 | 3 |
| -4 | 24 | -12 | 24 |

At `x = -4` the roles swap: the previous `cur_min` of `-6` becomes the new
`cur_max` of `24`, which is why the running minimum has to be carried even though
it never contributes a positive product of its own.

Time complexity: O(n) - one pass, each element used once.
Space complexity: O(1) - three running values, no arrays allocated.

Tests: `python3 tests/test_lc152.py`