import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_283_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_283.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def _move(nums):
    """Run moveZeroes() and return the same list, so callers can compare."""
    Solution().moveZeroes(nums)
    return nums


def test_move_zeroes_typical():
    assert _move([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_move_zeroes_second_example():
    assert _move([0]) == [0]


def test_move_zeroes_all_zeroes():
    assert _move([0, 0, 0, 0]) == [0, 0, 0, 0]


if __name__ == "__main__":
    test_move_zeroes_typical()
    test_move_zeroes_second_example()
    test_move_zeroes_all_zeroes()
    print("All tests passed for LC-283")
