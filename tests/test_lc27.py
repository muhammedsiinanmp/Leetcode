import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from arrays.LC_27 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_27", os.path.join(repo_root, "arrays", "LC_27.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1], 1, 0, []),
        ([], 1, 0, []),
        ([1, 2, 3], 4, 3, [1, 2, 3]),
    ]
    for nums, val, expected_k, expected_prefix in cases:
        arr = nums[:]
        k = sol.removeElement(arr, val)
        assert k == expected_k, f"nums={nums}, val={val} => got {k}, expected {expected_k}"
        assert arr[:k] == expected_prefix, f"nums={nums}, val={val} => arr[:k]={arr[:k]}, expected {expected_prefix}"
        assert all(x != val for x in arr[:k])

if __name__ == '__main__':
    run_tests()
    print('All LC-27 tests passed')
