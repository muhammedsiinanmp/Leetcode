class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates in-place from sorted array and return new length.

        Uses two-pointer technique: write_index tracks position to write the next
        unique value. Iterate read pointer and copy when new value encountered.
        """
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write
