import os
import sys

# Running this file directly puts tests/ on sys.path rather than the repo
# root, so the top-level solution directories are not importable without
# adding the root explicitly.
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

from strings.LC_415 import Solution


def test_add_strings():
    s = Solution()
    assert s.addStrings("123", "456") == "579"
    assert s.addStrings("99", "1") == "100"
    assert s.addStrings("0", "0") == "0"
    assert s.addStrings("1", "999") == "1000"
    assert s.addStrings("873", "9876") == "10749"


if __name__ == "__main__":
    test_add_strings()
    print("All tests passed for LC415")
