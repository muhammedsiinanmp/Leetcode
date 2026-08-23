class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """Remove all occurrences of val in-place and return new length.

        Uses the standard two-pointer approach: keep a write index for valid
        elements, and overwrite any values equal to val with later non-val items.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
