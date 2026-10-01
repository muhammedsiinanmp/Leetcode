import os
import sys

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# Load by path: the solution filename contains spaces and cannot be
# imported as a module by name.
import importlib.util

spec = importlib.util.spec_from_file_location(
    "LC_1512", os.path.join(repo_root, "arrays", "Number of good pairs.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
Solution = mod.Solution

sol = Solution()


def run_tests():
    cases = [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([], 0),
        ([1], 0),
        ([7, 7, 7, 8, 8, 9], 4),
    ]

    for nums, expected in cases:
        res = sol.numIdenticalPairs(list(nums))
        assert res == expected, f"nums={nums} => got {res}, expected {expected}"


if __name__ == '__main__':
    run_tests()
    print('All LC-1512 tests passed')
