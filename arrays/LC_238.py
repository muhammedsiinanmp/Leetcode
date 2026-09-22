class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Return each index's product without using division."""
        products = [1] * len(nums)
        prefix = 1

        for index, value in enumerate(nums):
            products[index] = prefix
            prefix *= value

        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            products[index] *= suffix
            suffix *= nums[index]

        return products
