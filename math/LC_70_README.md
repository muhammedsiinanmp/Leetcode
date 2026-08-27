LC-70: Climbing Stairs

Approach:
- Dynamic programming: the number of ways to reach step i is ways[i-1] + ways[i-2].
- Implement iteratively with two variables to achieve O(1) extra space.

Time complexity: O(n)
Space complexity: O(1)
