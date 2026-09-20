import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_169_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_169.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_majority_element():
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([7]) == 7
    assert solution.majorityElement([1, 1, 1, 2, 2]) == 1


if __name__ == "__main__":
    test_majority_element()
    print("All tests passed for LC169")
