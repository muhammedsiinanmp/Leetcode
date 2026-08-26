import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from arrays.LC_66 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_66", os.path.join(repo_root, "arrays", "LC_66.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
        ([9,9], [1,0,0]),
        ([0], [1]),
    ]
    for digits, expected in cases:
        res = sol.plusOne(digits[:])
        assert res == expected, f"digits={digits} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-66 tests passed')
