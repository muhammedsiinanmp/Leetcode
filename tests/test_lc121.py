import importlib.util
import os

# Import by file path to be robust to package/module names
spec = importlib.util.spec_from_file_location(
    "LC_121_module",
    os.path.join(os.path.dirname(__file__), '..', 'arrays', 'LC_121.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_max_profit():
    s = Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0
    assert s.maxProfit([1,2,3,4,5]) == 4
    assert s.maxProfit([2,4,1]) == 2


if __name__ == "__main__":
    test_max_profit()
    print("All tests passed for LC121")
