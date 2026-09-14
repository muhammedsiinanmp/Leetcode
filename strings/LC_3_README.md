LC 3 - Longest Substring Without Repeating Characters

Problem: Given a string, find the length of the longest substring without repeating characters.

Approach:
- Maintain a sliding window containing unique characters.
- Record each character's latest index and move the window start past a repeated character.

Time complexity: O(n)
Space complexity: O(min(n, character set size))
