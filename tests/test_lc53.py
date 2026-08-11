import sys
import os

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ensure arrays package path
sys.path.insert(0, repo_root)

# Attempt import of the solution module
try:
    # prefer file with dash replaced by underscore if present
    from arrays.LC_53 import Solution
except Exception:
    try:
        from arrays.LC_53 import Solution as Solution2
        Solution = Solution2
    except Exception:
        # fallback: import by file path
        import importlib.util
        spec = importlib.util.spec_from_file_location("LC_53", os.path.join(repo_root, "arrays", "LC-53.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([-1], -1),
        ([-2,-1], -1),
        ([5,4,-1,7,8], 23),
    ]

    for nums, expected in cases:
        res = sol.maxSubArray(nums)
        assert res == expected, f"nums={nums} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-53 tests passed')
