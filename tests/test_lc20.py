import importlib.util
import os

# Import by file path to avoid any module name issues
spec = importlib.util.spec_from_file_location(
    "LC_20_module",
    os.path.join(os.path.dirname(__file__), '..', 'strings', 'LC_20.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_is_valid():
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
    assert s.isValid("") is True


if __name__ == "__main__":
    test_is_valid()
    print("All tests passed for LC20")
