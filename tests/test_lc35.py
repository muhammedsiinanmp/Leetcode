import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from arrays.LC_35 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_35", os.path.join(repo_root, "arrays", "LC_35.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 1, 0),
        ([1], 0, 0),
    ]
    for nums, target, expected in cases:
        res = sol.searchInsert(nums, target)
        assert res == expected, f"nums={nums}, target={target} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-35 tests passed')
