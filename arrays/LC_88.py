class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Merge nums2 into nums1 in-place, keeping the result sorted."""
        left = m - 1
        right = n - 1
        write = m + n - 1

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[write] = nums1[left]
                left -= 1
            else:
                nums1[write] = nums2[right]
                right -= 1
            write -= 1
