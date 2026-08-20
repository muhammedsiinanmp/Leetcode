import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_58 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_58", os.path.join(repo_root, "strings", "LC_58.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 7),
        ("a", 1),
        ("", 0),
    ]
    for s, expected in cases:
        res = sol.lengthOfLastWord(s)
        assert res == expected, f"s={s!r} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-58 tests passed')
