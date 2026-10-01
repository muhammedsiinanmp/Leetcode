"""
1365. How Many Numbers Are Smaller Than the Current Number
Category: Arrays
Difficulty: Easy

Approach:
For each element, count how many elements in the array are strictly smaller
than it, using a nested loop.

Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary, excluding the output list
"""
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            output.append(count)
        return output
