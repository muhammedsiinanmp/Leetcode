import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_704_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_704.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_search():
    solution = Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([], 0) == -1
    assert solution.search([5], 5) == 0
    assert solution.search([5], -5) == -1
    assert solution.search([-10, -4, -1], -10) == 0
