class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """Rotate nums to the right by k steps, in place.

        LeetCode wants no return value here: the caller observes the change
        through the same list object, so the mutation must happen on `nums`
        itself rather than on a copy.

        k is reduced modulo len(nums) first, because rotating by a full lap
        (or several) leaves the array unchanged and a raw k could be larger
        than the list.
        """
        n = len(nums)
        if n <= 1:
            return

        k %= n
        if k == 0:
            return

        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)

    @staticmethod
    def _reverse(nums: list[int], left: int, right: int) -> None:
        """Reverse nums[left:right + 1] in place."""
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
