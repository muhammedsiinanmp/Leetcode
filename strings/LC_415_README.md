LC 415 - Add Strings

Problem: Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2 as a string without converting the whole strings to integers.

Approach:
- Process both strings from right to left, add corresponding digits plus carry.
- Append computed digit characters to a result list and reverse at the end.

Time complexity: O(max(n, m)) where n and m are lengths of the inputs.
Space complexity: O(max(n, m)) for the result.