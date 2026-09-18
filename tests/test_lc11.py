import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_11_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_11.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_max_area():
    solution = Solution()
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([1, 2, 1]) == 2
    assert solution.maxArea([]) == 0


if __name__ == "__main__":
    test_max_area()
    print("All tests passed for LC11")
