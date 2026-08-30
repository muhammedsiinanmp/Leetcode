LC-28: Implement strStr()

Approach:
- Use a sliding window to check each substring of haystack of length len(needle).
- Return the start index when a match is found. If needle is empty, return 0.
- For performance on large inputs consider KMP or other linear-time algorithms.

Time complexity: O(n*m) with naive slicing (n = len(haystack), m = len(needle)).
Space complexity: O(1) extra (slicing creates temporary strings of length m).
