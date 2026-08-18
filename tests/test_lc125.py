import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_125 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_125", os.path.join(repo_root, "strings", "LC_125.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        ("0P", False),
        ("a.", True),
    ]
    for s, expected in cases:
        res = sol.isPalindrome(s)
        assert res == expected, f"s={s!r} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-125 tests passed')
