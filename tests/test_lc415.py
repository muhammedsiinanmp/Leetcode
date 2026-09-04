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
