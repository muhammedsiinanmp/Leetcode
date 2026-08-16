import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_242 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_242", os.path.join(repo_root, "strings", "LC-242.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aacc", "ccaa", True),
        ("", "", True),
    ]
    for s, t, expected in cases:
        res = sol.isAnagram(s, t)
        assert res == expected, f"s={s}, t={t} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-242 tests passed')
