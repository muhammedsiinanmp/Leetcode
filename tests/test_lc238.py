import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_238_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_238.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_product_except_self():
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf([2, 3]) == [3, 2]
    assert solution.productExceptSelf([0, 0]) == [0, 0]


if __name__ == "__main__":
    test_product_except_self()
    print("All tests passed for LC238")
