from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Return the k values that occur most often."""
        frequencies = Counter(nums)
        return [
            value
            for frequency, value in heapq.nlargest(
                k, ((frequency, value) for value, frequency in frequencies.items())
            )
        ]
