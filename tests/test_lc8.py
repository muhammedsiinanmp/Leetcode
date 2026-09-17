import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_8_module",
    os.path.join(os.path.dirname(__file__), "..", "strings", "LC_8.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_my_atoi():
    solution = Solution()
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("-91283472332") == -(2**31)
    assert solution.myAtoi("91283472332") == 2**31 - 1
    assert solution.myAtoi("+1") == 1


if __name__ == "__main__":
    test_my_atoi()
    print("All tests passed for LC8")
