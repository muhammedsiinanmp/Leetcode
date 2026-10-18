class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """Return True if n flowers can be planted without touching.

        Greedy left-to-right scan: a plot is usable exactly when it is empty
        and both neighbours are empty (the plot just before, and the plot just
        after). Planting as early as possible never hurts a later plot, because
        the only plot a new flower can block is the next one, and the greedy
        choice already claims this one before the next is considered.

        The neighbours are read from the mutated flowerbed, so a flower planted
        at i is seen as occupied when i + 1 is examined. Out-of-range neighbours
        are treated as empty by the bounds checks.

        Complexity: O(n) time, O(1) extra space.
        """
        for index, plot in enumerate(flowerbed):
            if plot != 0:
                continue
            left_empty = index == 0 or flowerbed[index - 1] == 0
            right_empty = index == len(flowerbed) - 1 or flowerbed[index + 1] == 0
            if left_empty and right_empty:
                flowerbed[index] = 1
                n -= 1
                if n <= 0:
                    return True

        return n <= 0
