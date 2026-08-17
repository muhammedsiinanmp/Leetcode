import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# import the solution
try:
    from strings.LC_1047 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_1047", os.path.join(repo_root, "strings", "LC_1047.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("abbaca", "ca"),
        ("", ""),
        ("a", "a"),
        ("aa", ""),
        ("azxxzy", "ay"),
    ]
    for s, expected in cases:
        res = sol.removeDuplicates(s)
        assert res == expected, f"s={s} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-1047 tests passed')
