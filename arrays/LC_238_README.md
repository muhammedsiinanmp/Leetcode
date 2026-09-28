LC 238 - Product of Array Except Self

Problem: Given an integer array, return an array where each element is the product of all the other elements, without using division.

Approach:
- Store the product of all values to the left of each index in the result.
- Traverse from right to left, multiplying each result by the product of all values to its right.
- This naturally handles zero and negative values without special cases.

Time complexity: O(n)
Space complexity: O(1) extra space, excluding the returned array
