LC 7 - Reverse Integer

Problem: Given a signed 32-bit integer, return its digits reversed. Return 0 if the reversed value falls outside the signed 32-bit range.

Approach:
- Preserve the sign, reverse the decimal digits, and restore the sign.
- Check the result against the signed 32-bit bounds before returning it.

Time complexity: O(n), where n is the number of digits.
Space complexity: O(n) for the string representation.
