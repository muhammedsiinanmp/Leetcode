LC 605 - Can Place Flowers

Problem: Given a flowerbed represented as an integer array of 0's (empty) and
1's (planted), return True if n new flowers can be planted such that no two
flowers are adjacent. New flowers may only go into empty plots.

Approach:
- Scan the bed once from left to right.
- A plot at index i can take a flower when it is empty and both of its
  neighbours are empty. The neighbours are checked with bounds guards, so the
  two ends of the bed only have one real neighbour and the missing side counts
  as empty.
- When a plot qualifies, plant immediately (set it to 1) and decrement n. The
  next iteration then sees this plot as occupied and cannot plant next to it,
  which enforces the no-adjacent rule without any extra bookkeeping.
- Return as soon as n reaches zero, otherwise return whether n has been
  satisfied by the end of the scan.

Time complexity: O(n) - a single pass over the bed, since planting early only
ever removes work.
Space complexity: O(1) extra space; the bed is mutated in place and only the
remaining count n is tracked.
