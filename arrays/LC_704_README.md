# LC 704 - Binary Search

Given an ascending sorted integer array and a target, return the target's index
if it exists, or `-1` otherwise.

Approach:
- Keep a search interval bounded by `left` and `right`.
- Compare the target with the middle element and discard the half that cannot
  contain it.
- Stop when the target is found or the interval is empty.

Time complexity: O(log n)
Space complexity: O(1)
