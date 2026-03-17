"""
Leetcode Problem 1 - Two Sum
Category : Hash map
Difficculty : Easy

Problem
-------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Approach
--------
Created a map which stores index and values , And if the complement number in the map
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        res = []
        for index,value in enumerate(nums):
            if target - value in obj:
                res.extend([obj[target - value],index])
            obj[value] = index
        return res

s1 = Solution()
print(s1.twoSum([2,7,11,15],9))