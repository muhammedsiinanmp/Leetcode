"""
121. Best Time to Buy and Sell Stock
Single-pass O(n) solution tracking minimum price and max profit.

Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                # potential profit if sold today
                max_profit = max(max_profit, p - min_price)

        return max_profit


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2], 1),
        ([], 0),
    ]
    for arr, expected in samples:
        print(arr, sol.maxProfit(arr), expected)
