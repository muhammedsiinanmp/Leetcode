import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_28 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_28", os.path.join(repo_root, "strings", "LC_28.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("", "a", -1),
        ("abc", "", 0),
        ("mississippi", "issip", 4),
    ]
    for hay, needle, expected in cases:
        res = sol.strStr(hay, needle)
        assert res == expected, f"hay={hay!r}, needle={needle!r} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-28 tests passed')
