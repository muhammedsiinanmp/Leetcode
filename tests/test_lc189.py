import importlib.util
import os


spec = importlib.util.spec_from_file_location(
    "LC_189_module",
    os.path.join(os.path.dirname(__file__), "..", "arrays", "LC_189.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def test_rotate_placeholder():
    assert hasattr(Solution, "rotate")


if __name__ == "__main__":
    test_rotate_placeholder()
    print("All tests passed for LC-189")
