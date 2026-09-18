LC 11 - Container With Most Water

Problem: Given vertical lines represented by an array of heights, find two lines that contain the most water.

Approach:
- Start with pointers at both ends of the array.
- Compute the area and move the pointer at the shorter line inward, because moving the taller line cannot improve the limiting height.

Time complexity: O(n)
Space complexity: O(1)
