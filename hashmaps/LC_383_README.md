LC-383: Ransom Note

Approach:
- Count characters in magazine using collections.Counter.
- For each character in ransomNote, ensure magazine has remaining count > 0; decrement as used.
- Return True if all characters in ransomNote can be supplied by magazine.

Time complexity: O(n + m) where n,m are the lengths of ransomNote and magazine.
Space complexity: O(k) where k is alphabet size (bounded).
