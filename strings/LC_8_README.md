LC 8 - String to Integer (atoi)

Problem: Convert a string to a 32-bit signed integer while following whitespace, sign, digit, and overflow rules.

Approach:
- Skip leading spaces, read an optional sign, and accumulate consecutive digits.
- Clamp the result immediately when it exceeds the signed 32-bit range.

Time complexity: O(n)
Space complexity: O(1)
