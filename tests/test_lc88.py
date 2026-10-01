import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_88_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_88.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_merge_sorted_array():
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [-3, 0, 0, 0]
    solution.merge(nums1, 1, [-3, 2, 2], 3)
    assert nums1 == [-3, -3, 2, 2]

    nums1 = []
    solution.merge(nums1, 0, [], 0)
    assert nums1 == []


if __name__ == "__main__":
    test_merge_sorted_array()
    print("All tests passed for LC-88")
