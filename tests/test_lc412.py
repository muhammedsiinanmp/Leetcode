import os
import sys

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

# Load by path: the solution filename contains spaces and cannot be
# imported as a module by name.
import importlib.util

spec = importlib.util.spec_from_file_location(
    "LC_412", os.path.join(repo_root, "math", "FizzBuzz.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
Solution = mod.Solution

sol = Solution()


def run_tests():
    assert sol.fizzBuzz(1) == ["1"]
    assert sol.fizzBuzz(3) == ["1", "2", "Fizz"]
    assert sol.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert sol.fizzBuzz(0) == []
    assert sol.fizzBuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
        "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    assert sol.fizzBuzz(100)[-1] == "Buzz"

    # Regression guard: multiples of 3 must be "Fizz", never the raw number.
    # The i % 3 branch was previously commented out.
    for i in range(1, 101):
        if i % 15 == 0:
            expected = "FizzBuzz"
        elif i % 3 == 0:
            expected = "Fizz"
        elif i % 5 == 0:
            expected = "Buzz"
        else:
            expected = str(i)
        assert sol.fizzBuzz(i)[-1] == expected, f"i={i} => got {sol.fizzBuzz(i)[-1]}"


if __name__ == '__main__':
    run_tests()
    print('All LC-412 tests passed')
