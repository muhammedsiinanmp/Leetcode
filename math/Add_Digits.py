"""
LeetCode Problem: 258 - Add Digits
Category: Math
Difficulty: Easy

Problem
-------
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

Approach 1 (Optimal - Digital Root)
-----------------------------------
Instead of repeatedly summing digits, we can use a mathematical property called the **Digital Root**.

Rules:
1. If num == 0 → return 0
2. Otherwise → result = 1 + (num - 1) % 9

This works because numbers follow a repeating pattern modulo 9.

Example:
38 → 3 + 8 = 11 → 1 + 1 = 2  
38 % 9 = 2

Time Complexity
---------------
O(1)

Space Complexity
----------------
O(1)

Approach 2 (Iterative)
----------------------
1. Keep summing digits until the number becomes a single digit.
2. Extract digits using modulo (`num % 10`)
3. Remove digits using integer division (`num //= 10`)
4. Repeat until num < 10

Time Complexity
---------------
O(log n)

Space Complexity
----------------
O(1)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        # Digital Root Approach (Optimal)
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


# Iterative Approach (for understanding)

# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num >= 10:
#             total = 0
#             while num > 0:
#                 total += num % 10
#                 num //= 10
#             num = total
#         return num