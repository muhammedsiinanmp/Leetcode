import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_7_module",
    os.path.join(os.path.dirname(__file__), "..", "math", "LC_7.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_reverse():
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
    assert solution.reverse(1534236469) == 0


if __name__ == "__main__":
    test_reverse()
    print("All tests passed for LC7")
