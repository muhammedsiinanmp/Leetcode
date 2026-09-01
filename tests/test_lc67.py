import os
import sys
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

try:
    from strings.LC_67 import Solution
except Exception:
    import importlib.util
    spec = importlib.util.spec_from_file_location("LC_67", os.path.join(repo_root, "strings", "LC_67.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Solution = mod.Solution

sol = Solution()

def run_tests():
    cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "111", "1000"),
        ("1111", "1", "10000"),
    ]
    for a, b, expected in cases:
        res = sol.addBinary(a, b)
        assert res == expected, f"a={a}, b={b} => got {res}, expected {expected}"

if __name__ == '__main__':
    run_tests()
    print('All LC-67 tests passed')
