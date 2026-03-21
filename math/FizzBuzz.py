"""
LeetCode Problem: 412 - Fizz Buzz
Category: Math / Simulation
Difficulty: Easy

Problem
-------
Given an integer `n`, return a string array `answer` (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by both 3 and 5
- answer[i] == "Fizz" if i is divisible by 3
- answer[i] == "Buzz" if i is divisible by 5
- answer[i] == str(i) otherwise

Approach
--------
1. Iterate from 1 to n.
2. For each number:
   - Check if divisible by both 3 and 5 → append "FizzBuzz"
   - Else if divisible by 3 → append "Fizz"
   - Else if divisible by 5 → append "Buzz"
   - Otherwise → append the number as string
3. Return the result list.

Note:
- Always check for (3 and 5) first to avoid missing "FizzBuzz".

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result


# Alternative Approach (String Accumulation)

# class Solution:
#     def fizzBuzz(self, n: int) -> list[str]:
#         result = []
#
#         for i in range(1, n + 1):
#             s = ""
#
#             if i % 3 == 0:
#                 s += "Fizz"
#             if i % 5 == 0:
#                 s += "Buzz"
#
#             result.append(s if s else str(i))
#
#         return result