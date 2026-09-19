import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_49_module",
    os.path.join(os.path.dirname(__file__), "..", "hashmaps", "LC_49.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def normalize(groups):
    return sorted(sorted(group) for group in groups)


def test_group_anagrams():
    solution = Solution()
    assert normalize(
        solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    ) == normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert normalize(solution.groupAnagrams([""])) == [[""]]
    assert normalize(solution.groupAnagrams(["a"])) == [["a"]]
    assert normalize(solution.groupAnagrams([])) == []


if __name__ == "__main__":
    test_group_anagrams()
    print("All tests passed for LC49")
