class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return indices of the two numbers such that they add up to target.

        Use a hashmap to store seen values -> index and check complement in one pass.
        """
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        # problem guarantees exactly one solution; raise otherwise
        raise ValueError("No two sum solution")
