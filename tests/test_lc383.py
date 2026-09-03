import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from hashmaps.LC_383 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_383", os.path.join(repo_root, "hashmaps", "LC_383.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "", True),
        ("abc", "cbad", True),
    ]
    for r, m, expected in cases:
        res = sol.canConstruct(r, m)
        assert res == expected, f"ransomNote={r!r}, magazine={m!r} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-383 tests passed')
