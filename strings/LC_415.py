class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """Add two non-negative integer numbers represented as strings and
        return their sum as a string without converting directly to integers.

        Process digits from right to left with carry, build result list and
        reverse/join at the end.
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            x = ord(num1[i]) - 48 if i >= 0 else 0
            y = ord(num2[j]) - 48 if j >= 0 else 0
            s = x + y + carry
            res.append(chr(48 + (s % 10)))
            carry = s // 10
            i -= 1
            j -= 1
        return ''.join(reversed(res))
