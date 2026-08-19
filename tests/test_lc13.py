import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_13 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_13", os.path.join(repo_root, "strings", "LC_13.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("", 0),
    ]
    for s, expected in cases:
        res = sol.romanToInt(s)
        assert res == expected, f"s={s!r} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-13 tests passed')
