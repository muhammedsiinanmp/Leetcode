LC 54 - Spiral Matrix

Problem: Given an m x n matrix, return all of its elements in clockwise
spiral order.

Approach:
- Track four boundaries: `top`, `bottom`, `left` and `right`, which shrink inwards
  one full ring at a time.
- Each pass consumes one edge of the remaining rectangle, then moves that edge's
  boundary past the values just visited:
  - top edge, left to right, then `top += 1`
  - right edge, top to bottom, then `right -= 1`
  - bottom edge, right to left, then `bottom -= 1`
  - left edge, bottom to top, then `left += 1`
- Repeat while `top <= bottom and left <= right`.
- The bottom edge is only walked when `top <= bottom`, and the left edge only when
  `left <= right`. Without those guards the final pass would re-emit the
  bottom-left corner: on a 2x2 matrix the bottom edge has already been consumed by
  the right edge, and on a single remaining row or column the two opposing edges
  overlap. Those cases are exactly where a naive implementation duplicates values.

Time complexity: O(m * n) - every element is appended exactly once.
Space complexity: O(1) extra space beyond the O(m * n) result list.