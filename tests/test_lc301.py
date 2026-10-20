import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_301_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_301.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def remove(nums):
    """Run removeDuplicates on a copy and return (k, first k values)."""
    arr = list(nums)
    solution = Solution()
    k = solution.removeDuplicates(arr)
    return k, arr[:k]


def test_all_identical():
    assert remove([7, 7, 7, 7]) == (1, [7])


def test_two_distinct_runs():
    assert remove([1, 1, 2]) == (2, [1, 2])


def test_leetcode_example():
    assert remove([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == (5, [0, 1, 2, 3, 4])


def test_already_distinct():
    assert remove([1, 2, 3, 4, 5]) == (5, [1, 2, 3, 4, 5])


def test_single_element():
    assert remove([42]) == (1, [42])


def test_empty_input():
    assert remove([]) == (0, [])


def test_negatives_and_zero():
    assert remove([-3, -3, -1, 0, 0, 2]) == (4, [-3, -1, 0, 2])


def test_leading_duplicates():
    assert remove([5, 5, 5, 9]) == (2, [5, 9])


def test_matches_leetcode_26_on_same_input():
    # LC-26 and LC-301 share a contract, so the outputs must agree.
    import importlib.util as _util

    spec26 = _util.spec_from_file_location(
        "LC_26_module",
        os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_26.py"),
    )
    module26 = _util.module_from_spec(spec26)
    spec26.loader.exec_module(module26)

    for nums in ([1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [], [1], [1, 2, 3]):
        a = list(nums)
        b = list(nums)
        k26 = module26.Solution().removeDuplicates(a)
        k301 = Solution().removeDuplicates(b)
        assert (k26, a[:k26]) == (k301, b[:k301]), f"mismatch on {nums}"


if __name__ == "__main__":
    test_all_identical()
    test_two_distinct_runs()
    test_leetcode_example()
    test_already_distinct()
    test_single_element()
    test_empty_input()
    test_negatives_and_zero()
    test_leading_duplicates()
    test_matches_leetcode_26_on_same_input()
    print("All tests passed for LC-301")