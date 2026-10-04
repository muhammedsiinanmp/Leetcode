class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """Return the largest product of a non-empty contiguous subarray of nums.

        nums contains at least one element and the subarray must not be empty,
        so the answer is never 0 by default: an input such as [-3, -4] has the
        answer 12 even though every individual element is negative.
        """
        best = cur_max = cur_min = nums[0]

        for x in nums[1:]:
            if x < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            best = max(best, cur_max)

        return best