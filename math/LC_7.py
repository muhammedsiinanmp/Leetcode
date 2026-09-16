class Solution:
    def reverse(self, x: int) -> int:
        """Reverse x, returning zero when the signed 32-bit range is exceeded."""
        sign = -1 if x < 0 else 1
        reversed_digits = int(str(abs(x))[::-1])
        result = sign * reversed_digits
        return result if -(2**31) <= result <= 2**31 - 1 else 0
