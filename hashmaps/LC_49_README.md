LC 49 - Group Anagrams

Problem: Given an array of strings, group the strings that are anagrams of one another.

Approach:
- Sort the characters in each string to create a canonical signature.
- Store strings with the same signature in a hash map.
- Return the map's grouped values.

Time complexity: O(n * k log k), where n is the number of strings and k is the
maximum string length.
Space complexity: O(n * k) for the grouped strings and signatures.
