"""
LeetCode 1512 - Number of Good Pairs
Category: Array
Difficulty: Easy

Approach:
Use a nested loop to compare each pair of elements.
If they are equal, increment the count.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    res += 1

        return res