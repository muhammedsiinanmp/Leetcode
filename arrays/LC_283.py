class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """Move all zeroes to the end while keeping non-zero order.

        LeetCode mutates `nums` in place and expects no return value.

        A single write pointer walks just behind the read pointer. Every
        non-zero value is compacted to the front, and once the read pointer
        is exhausted the tail is overwritten with zeroes. Each element is
        visited once and nothing is ever shifted, so the original relative
        order of the non-zero values is preserved.

        Complexity: O(n) time over the length of nums, O(1) extra space
        beyond the single write index.
        """
        write = 0
        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1

        for index in range(write, len(nums)):
            nums[index] = 0
