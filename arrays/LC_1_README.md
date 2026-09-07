LC 1 - Two Sum

Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Approach:
- Use a hashmap (value -> index) and iterate once, checking if complement exists.
- This yields O(n) time and O(n) extra space.

Time complexity: O(n)
Space complexity: O(n)
