import importlib.util
import os

# Import by file path to avoid any package name conflicts
spec = importlib.util.spec_from_file_location(
    "LC_1_module",
    os.path.join(os.path.dirname(__file__), '..', 'arrays', 'LC_1.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_two_sum():
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [0,1]
    assert s.twoSum([3,2,4], 6) == [1,2]
    assert s.twoSum([3,3], 6) == [0,1]


if __name__ == "__main__":
    test_two_sum()
    print("All tests passed for LC1")
