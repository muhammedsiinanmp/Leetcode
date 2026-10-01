import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_347_module",
    os.path.join(os.path.dirname(__file__), "..", "hashmaps", "LC_347.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_top_k_frequent():
    solution = Solution()
    assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert set(solution.topKFrequent([1], 1)) == {1}
    assert set(solution.topKFrequent([-1, -1, 2, 2, 2, 3], 2)) == {2, -1}
    assert set(solution.topKFrequent([4, 4, 5, 5], 2)) == {4, 5}


if __name__ == "__main__":
    test_top_k_frequent()
    print("All tests passed for LC347")
