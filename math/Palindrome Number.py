"""
LeetCode Problem: 9 - Palindrome Number
Category: Math
Difficulty: Easy

Problem
-------
Given an integer `x`, return true if it is a palindrome, and false otherwise.

A palindrome number reads the same backward as forward.

Approach
--------
1. Negative numbers are not palindrome.
2. Reverse the number using modulo and division.
3. Compare the reversed number with the original.

Time Complexity
---------------
O(log n)

Space Complexity
----------------
O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num