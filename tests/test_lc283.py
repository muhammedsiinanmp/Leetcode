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


def test_move_zeroes_no_zeroes():
    assert _move([1, 2, 3]) == [1, 2, 3]


def test_move_zeroes_leading_zeroes():
    assert _move([0, 0, 1, 2]) == [1, 2, 0, 0]


def test_move_zeroes_preserves_relative_order():
    assert _move([4, 0, 5, 0, 6, 7]) == [4, 5, 6, 7, 0, 0]


def test_move_zeroes_mutates_in_place():
    """LeetCode inspects the caller's list, not a returned copy."""
    nums = [0, 1, 0, 3, 12]
    identity = id(nums)
    result = Solution().moveZeroes(nums)

    assert result is None
    assert id(nums) == identity
    assert nums == [1, 3, 12, 0, 0]


def test_move_zeroes_matches_stable_partition_oracle():
    """Cross-check against Python's stable partition."""
    import random

    for size in range(0, 9):
        for _ in range(25):
            original = [random.randint(0, 3) for _ in range(size)]
            expected = [v for v in original if v != 0] + [0] * original.count(0)
            nums = list(original)
            Solution().moveZeroes(nums)
            assert nums == expected, original


if __name__ == "__main__":
    test_move_zeroes_typical()
    test_move_zeroes_second_example()
    test_move_zeroes_all_zeroes()
    test_move_zeroes_no_zeroes()
    test_move_zeroes_leading_zeroes()
    test_move_zeroes_preserves_relative_order()
    test_move_zeroes_mutates_in_place()
    test_move_zeroes_matches_stable_partition_oracle()
    print("All tests passed for LC-283")
