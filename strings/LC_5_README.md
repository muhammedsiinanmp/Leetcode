LC 5 - Longest Palindromic Substring

Problem: Given a string, return the longest substring that reads the same forward and backward.

Approach:
- Treat every character and every gap between characters as a possible palindrome center.
- Expand around each center while matching characters, retaining the longest range.

Time complexity: O(n^2)
Space complexity: O(1), excluding the returned substring.
