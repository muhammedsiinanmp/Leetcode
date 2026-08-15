import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from arrays.LC_217 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_217", os.path.join(repo_root, "arrays", "LC-217.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
        ([], False),
    ]
    for arr, expected in cases:
        res = sol.containsDuplicate(arr)
        assert res == expected, f"arr={arr} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-217 tests passed')
