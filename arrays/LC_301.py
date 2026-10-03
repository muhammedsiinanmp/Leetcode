class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Compact distinct values to the front of nums in place and return their count.

        nums is sorted in non-decreasing order. After the call the first k
        entries are the distinct values in their original order, where k is
        the returned length; entries from index k on are undefined.
        """
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k