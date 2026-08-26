class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """Add one to the integer represented by the digits list and return
        the resulting digits list. Handles carry propagation in-place.
        """
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
            if carry == 0:
                break
        if carry:
            return [carry] + digits
        return digits
