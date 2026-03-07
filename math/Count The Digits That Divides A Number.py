"""
LeetCode Problem: 2520 - Count the Digits That Divide a Number
Category: Math
Difficulty: Easy

Problem
-------
Given an integer `num`, return the number of digits in `num` that divide `num`.

A digit `d` divides `num` if:
    num % d == 0

Note:
Digits equal to 0 cannot be used as divisors.

Approach
--------
1. Store the original number since we will modify `num` during iteration.
2. Extract digits one by one using modulo operation (`num % 10`).
3. Check if the digit is non-zero and divides the original number.
4. If it does, increment the counter.
5. Remove the last digit using integer division (`num // 10`).
6. Continue until all digits are processed.

Time Complexity
---------------
O(d)

d = number of digits in the number

Space Complexity
----------------
O(1)
"""


class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        original_num = num

        while num > 0:
            digit = num % 10

            if digit != 0 and original_num % digit == 0:
                result += 1

            num //= 10

        return result
    

# Normal Approach

# class Solution:
#     def countDigits(self, num: int) -> int:
#         res = 0
        # snum = str(num)
        # for i in snum:
        #     if num % int(i) == 0:
        #         res += 1
        # return res
