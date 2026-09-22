LC 238 - Product of Array Except Self

Problem: Given an integer array, return an array where each position contains
the product of every input value except the value at that position.

Approach:
- Store the product of all values to the left of each index.
- Traverse from right to left and multiply each position by its suffix product.
- This avoids division and handles zero values naturally.

Time complexity: O(n).
Space complexity: O(1) auxiliary space, excluding the returned array.
