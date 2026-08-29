import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from arrays.LC_26 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_26", os.path.join(repo_root, "arrays", "LC_26.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([1,1,2], [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4]),
        ([], []),
        ([1], [1]),
        ([1,2,3], [1,2,3]),
    ]
    for nums, expected_prefix in cases:
        arr = nums[:]
        k = sol.removeDuplicates(arr)
        assert k == len(expected_prefix), f"nums={nums} => got k={k}, expected {len(expected_prefix)}"
        assert arr[:k] == expected_prefix, f"nums={nums} => arr[:k]={arr[:k]}, expected {expected_prefix}"

if __name__ == '__main__':
    run_tests()
    print('All LC-26 tests passed')
