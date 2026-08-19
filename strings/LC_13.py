class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert a Roman numeral to integer.

        Uses a mapping and processes characters left-to-right, subtracting
        when a smaller value precedes a larger one.
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for ch in reversed(s):
            val = values.get(ch, 0)
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total
