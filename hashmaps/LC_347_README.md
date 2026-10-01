LC 347 - Top K Frequent Elements

Problem: Given an integer array, return the `k` values that occur most often.

Approach:
- Count each value with a frequency map.
- Use a max heap over `(frequency, value)` pairs to select the `k` largest
  frequencies.
- Return only the selected values.

Time complexity: O(n + u log k), where `u` is the number of unique values.
Space complexity: O(u).
