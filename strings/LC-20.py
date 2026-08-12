"""
20. Valid Parentheses
Use a stack to verify matching pairs.
"""
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {')':'(', ']':'[', '}':'{'}
        stack: List[str] = []

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # ignore other characters (problem only contains these brackets)
                pass

        return not stack


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    for s, expected in samples:
        print(s, sol.isValid(s), expected)
