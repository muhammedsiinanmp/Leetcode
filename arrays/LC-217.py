"""
217. Contains Duplicate
Return True if any value appears at least twice in the array.

Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using a set to detect duplicates in O(n) time and O(n) space
        seen = set()
        for x in nums:
            # early return when a duplicate is found
            if x in seen:
                return True
            seen.add(x)
        # no duplicates found
        return False


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
    ]
    for arr, expected in samples:
        print(arr, sol.containsDuplicate(arr), expected)
