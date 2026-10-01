"""
15. 3Sum
Given an integer array nums, return all the unique triplets
[nums[i], nums[j], nums[k]] such that i, j and k are distinct indices and
nums[i] + nums[j] + nums[k] == 0. The solution set must not contain
duplicate triplets.

Example
-------
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Approach
--------
Sort the array, then fix each element as an anchor and search for the other
two with a two-pointer scan.

1. Sort nums. Sorting lets both pointers move monotonically inward, and it
   makes adjacent elements comparable so duplicate values can be skipped.
2. For each index i from 0 to n - 3:
   a. If nums[i] > 0 the sum of three remaining values can no longer reach 0,
      so stop early.
   b. If nums[i] == nums[i - 1] the anchor is a repeat, so skip it. Without
      this the same triplets would be produced several times over.
   c. Place left at i + 1 and right at n - 1 and compare the sum:
      - sum < 0  -> too small, advance left to increase the sum
      - sum > 0  -> too large, decrease right to reduce the sum
      - sum == 0 -> record the triplet, then skip past duplicate values on
                    both sides before moving both pointers inward.
3. Duplicates are skipped in three places: repeated anchors, repeated left
   values, and repeated right values.

Complexity
----------
Time:  O(n^2). The sort is O(n log n); the outer loop runs at most n times and
      each two-pointer scan moves the pointers a total of O(n) steps, so the
      scan dominates.
Space: O(n) in the worst case for the auxiliary buffer Python's sort may use,
      plus O(1) for the scan itself. The returned list is excluded, and can
      hold O(n^2) triplets in the worst case.
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

            result.extend(self._pairs_for(nums, i))

        return result

    def _pairs_for(self, nums: List[int], i: int) -> List[List[int]]:
        """Two-pointer scan for the pairs that complete the anchor at index i."""
        pairs = []
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                pairs.append([nums[i], nums[left], nums[right]])

                # Move both pointers inward, skipping duplicates on each side.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

        return pairs


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
