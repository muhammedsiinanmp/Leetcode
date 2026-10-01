LC 169 - Majority Element

Problem: Given an array of integers, find the element that appears more than
half of the time.

Approach:
- Track a candidate and its vote count while scanning the array.
- Matching values add a vote; different values cancel a vote.
- Because a majority is guaranteed, the final candidate is the answer.

Time complexity: O(n).
Space complexity: O(1).
