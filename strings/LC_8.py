class Solution:
    def myAtoi(self, s: str) -> int:
        """Convert a string to a signed 32-bit integer following atoi rules."""
        index = 0
        length = len(s)
        while index < length and s[index] == " ":
            index += 1

        sign = 1
        if index < length and s[index] in "+-":
            sign = -1 if s[index] == "-" else 1
            index += 1

        value = 0
        lower = -(2**31)
        upper = 2**31 - 1
        while index < length and s[index].isdigit():
            value = value * 10 + ord(s[index]) - ord("0")
            signed_value = sign * value
            if signed_value < lower:
                return lower
            if signed_value > upper:
                return upper
            index += 1

        return sign * value
