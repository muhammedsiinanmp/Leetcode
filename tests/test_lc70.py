import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from math.LC_70 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_70", os.path.join(repo_root, "math", "LC_70.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
    ]
    for n, expected in cases:
        res = sol.climbStairs(n)
        assert res == expected, f"n={n} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-70 tests passed')
