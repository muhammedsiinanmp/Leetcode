LC-13: Roman to Integer

Approach:
- Create a value map for Roman numerals.
- Scan the string from right to left, accumulating values.
- If a numeral is less than the previous (to its right), subtract it; otherwise add it.
- This handles subtractive notation like IV (4) and IX (9).

Time complexity: O(n)
Space complexity: O(1)
