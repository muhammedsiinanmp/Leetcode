import os
import sys

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# The solution file name contains a dash, so load it by path.
import importlib.util

spec = importlib.util.spec_from_file_location(
    "LC_15", os.path.join(repo_root, "hashmaps", "LC-15.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
Solution = mod.Solution

sol = Solution()


def run_tests():
    cases = [
        # canonical example, note the duplicate -1 pair
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # too short to form a triplet
        ([], []),
        ([0], []),
        ([0, 1], []),
        # all zeros must yield exactly one triplet
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        # no valid triplet exists
        ([1, 2, 3], []),
        ([0, 1, 1], []),
        # all positive, early break
        ([1, 2, 3, 4], []),
        # all negative
        ([-3, -2, -1], []),
        # multiple triplets
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
         [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
          [-2, -2, 4], [-2, 0, 2]]),
        # single zero-sum triplet with duplicates around it
        ([-4, 2, 2, 2, 2], [[-4, 2, 2]]),
        # no zero-sum triplet despite a negative anchor
        ([-1, 1, 1, 2], []),
        # reversed input order must produce the same result
        ([1, 2, -1, -1], [[-1, -1, 2]]),
    ]

    for nums, expected in cases:
        res = sol.threeSum(list(nums))
        assert res == expected, f"nums={nums} => got {res}, expected {expected}"

    # Input must not be mutated in place.
    original = [3, -1, -1, 0, 2]
    snapshot = list(original)
    sol.threeSum(original)
    assert original == snapshot, f"input was mutated: {original} != {snapshot}"


if __name__ == '__main__':
    run_tests()
    print('All LC-15 tests passed')
