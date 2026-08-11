"""
53. Maximum Subarray
Kadane's algorithm O(n) solution.

Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            # Problem constraints guarantee at least one element, but be defensive
            return 0

        max_ending_here = nums[0]
        max_so_far = nums[0]

        for x in nums[1:]:
            # either extend the previous subarray or start fresh at current element
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


if __name__ == "__main__":
    # Quick manual tests
    sol = Solution()
    cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),  # example: subarray [4,-1,2,1]
        ([1], 1),
        ([-1], -1),
        ([-2,-1], -1),
        ([5,4,-1,7,8], 23),
    ]

    for nums, expected in cases:
        res = sol.maxSubArray(nums)
        print(f"nums={nums} => {res} (expected {expected})")
