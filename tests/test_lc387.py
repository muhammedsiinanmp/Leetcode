import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_387 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_387", os.path.join(repo_root, "strings", "LC_387.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        ("z", 0),
    ]
    for s, expected in cases:
        res = sol.firstUniqChar(s)
        assert res == expected, f"s={s!r} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-387 tests passed')
