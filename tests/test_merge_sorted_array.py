import os
import sys

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# Load by path: the solution filename contains spaces and cannot be
# imported as a module by name.
import importlib.util

spec = importlib.util.spec_from_file_location(
    "LC_88", os.path.join(repo_root, "arrays", "Merge_Sorted_Array.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
Solution = mod.Solution

sol = Solution()


def run_tests():
    # (nums1, m, nums2, n, expected nums1 after merge)
    cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([0], 0, [0], 1, [0]),
        # every element of nums1 is larger than every element of nums2
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        # interleave
        ([1, 0, 0, 0], 1, [2, 3, 4], 3, [1, 2, 3, 4]),
    ]

    for nums1, m, nums2, n, expected in cases:
        original1 = list(nums1)
        sol.merge(nums1, m, list(nums2), n)
        assert nums1 == expected, \
            f"nums1={original1}, m={m}, nums2={nums2} => got {nums1}, expected {expected}"


if __name__ == '__main__':
    run_tests()
    print('All LC-88 tests passed')
