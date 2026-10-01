import os
import sys

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# Load by path: the solution filename contains a dash and cannot be
# imported as a module by name.
import importlib.util

spec = importlib.util.spec_from_file_location(
    "LC_1365", os.path.join(repo_root, "arrays", "LC-1365.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
Solution = mod.Solution

sol = Solution()


def run_tests():
    cases = [
        ([8, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 0, 1, 2, 3, 4, 5, 6, 7, 9]),
        ([5, 5, 5, 5], [0, 0, 0, 0]),
        ([1], [0]),
        ([], []),
        # unsorted input, comparison is against the whole array
        ([3, 2, 1], [2, 1, 0]),
        # duplicates do not count as smaller
        ([2, 2, 2], [0, 0, 0]),
    ]

    for nums, expected in cases:
        res = sol.smallerNumbersThanCurrent(list(nums))
        assert res == expected, f"nums={nums} => got {res}, expected {expected}"


if __name__ == '__main__':
    run_tests()
    print('All LC-1365 tests passed')
