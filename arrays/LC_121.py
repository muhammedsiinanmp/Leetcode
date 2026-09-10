class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Return the max profit from a single buy/sell transaction.

        Track the minimum price seen so far and compute potential profit at each
        day, keeping the max.
        """
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
