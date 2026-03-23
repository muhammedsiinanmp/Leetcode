"""
LeetCode Problem: 88 - Merge Sorted Array
Category: Array / Two Pointers
Difficulty: Easy

Problem
-------
Merge two sorted arrays `nums1` and `nums2` into `nums1` in-place.

Approach
--------
Use three pointers from the end:

- p1 → last element of nums1 (m - 1)
- p2 → last element of nums2 (n - 1)
- pos → last position of nums1 (m + n - 1)

1. Compare elements from the end.
2. Place the larger one at the correct position.
3. Move pointers accordingly.
4. Continue until all elements of nums2 are placed.

Time Complexity
---------------
O(m + n)

Space Complexity
----------------
O(1)
"""


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, pos = m - 1, n - 1, m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1