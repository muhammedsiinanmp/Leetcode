import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# import the solution, with fallback to file-based import
try:
    from arrays.LC_121 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_121", os.path.join(repo_root, "arrays", "LC-121.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2], 1),
        ([], 0),
    ]
    for prices, expected in cases:
        res = sol.maxProfit(prices)
        assert res == expected, f"prices={prices} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-121 tests passed')
