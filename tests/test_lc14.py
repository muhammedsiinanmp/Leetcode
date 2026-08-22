import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_14 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_14", os.path.join(repo_root, "strings", "LC_14.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        ([], ""),
        (["a"], "a"),
        (["interspecies","interstellar","interstate"], "inters"),
    ]
    for arr, expected in cases:
        res = sol.longestCommonPrefix(arr)
        assert res == expected, f"arr={arr} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-14 tests passed')
