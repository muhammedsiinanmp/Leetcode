import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_344 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_344", os.path.join(repo_root, "strings", "LC_344.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        (list("hello"), list("olleh")),
        (list("Hannah"), list("hannaH")),
        ([], []),
        (["a"], ["a"]),
    ]
    for inp, expected in cases:
        arr = inp[:]
        sol.reverseString(arr)
        assert arr == expected, f"input={inp} => got {arr}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-344 tests passed')
