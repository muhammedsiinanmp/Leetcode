"""
15. 3Sum
Sort the array, then for each anchor element use two pointers to find the
remaining pair that completes a zero-sum triplet.

Time complexity: O(n^2)
Space complexity: O(n) worst case for Python's sort, O(1) for the scan
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting lets us move both pointers monotonically and makes duplicate
        # skipping straightforward.
        nums = sorted(nums)
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Once the anchor is positive no zero-sum triplet can start here.
            if nums[i] > 0:
                break

            # Skip repeated anchors so the same triplet is never emitted twice.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward, skipping duplicates on each side.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == "__main__":
    # Quick manual tests
    sol = Solution()
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
    ]

    for nums, expected in cases:
        res = sol.threeSum(nums)
        print(f"nums={nums} => {res} (expected {expected})")
