"""
LeetCode Problem: 169 - Majority Element
Category: Array
Difficulty: Easy

Problem
-------
Given an array `nums`, return the element that appears more than n/2 times.

Approach
--------
Use Boyer-Moore Voting Algorithm:

1. Keep a candidate and a count.
2. If count becomes 0 → choose a new candidate.
3. If current element == candidate → increase count.
4. Else → decrease count.
5. The final candidate is the majority element.

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(1)
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate