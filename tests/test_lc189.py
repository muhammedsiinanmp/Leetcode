import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_189_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_189.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def _rotate(nums, k):
    """Run rotate() and return a copy, so callers can compare results."""
    Solution().rotate(nums, k)
    return nums


def test_rotate_typical():
    assert _rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_second_example():
    assert _rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]


def test_rotate_zero_steps():
    assert _rotate([1, 2, 3], 0) == [1, 2, 3]


def test_rotate_full_lap():
    assert _rotate([1, 2, 3], 3) == [1, 2, 3]


def test_rotate_more_than_length():
    assert _rotate([1, 2, 3], 4) == [3, 1, 2]


def test_rotate_large_k():
    assert _rotate([1, 2], 5) == [2, 1]


def test_rotate_single_element():
    assert _rotate([42], 7) == [42]


def test_rotate_empty_list():
    assert _rotate([], 3) == []


def test_rotate_two_elements():
    assert _rotate([1, 2], 1) == [2, 1]


def test_rotate_matches_brute_force_oracle():
    """Cross-check the triple reverse against a naive rebuild."""
    for size in range(1, 9):
        original = list(range(size))
        for k in range(0, size * 3 + 1):
            expected = [original[(i - k) % size] for i in range(size)]
            assert _rotate(list(original), k) == expected, (original, k)


def test_rotate_mutates_in_place():
    """LeetCode checks the caller's list, not a returned copy."""
    nums = [1, 2, 3, 4, 5]
    identity = id(nums)
    result = Solution().rotate(nums, 2)

    assert result is None
    assert id(nums) == identity
    assert nums == [4, 5, 1, 2, 3]


if __name__ == "__main__":
    test_rotate_typical()
    test_rotate_second_example()
    test_rotate_zero_steps()
    test_rotate_full_lap()
    test_rotate_more_than_length()
    test_rotate_large_k()
    test_rotate_single_element()
    test_rotate_empty_list()
    test_rotate_two_elements()
    test_rotate_matches_brute_force_oracle()
    test_rotate_mutates_in_place()
    print("All tests passed for LC-189")
