LC 121 - Best Time to Buy and Sell Stock

Problem: Given an array prices where prices[i] is the price of a given stock on the ith day, return the maximum profit you can achieve from one transaction.

Approach:
- Track the minimum price seen so far and compute profit at each day: profit = price - min_price.
- Keep the maximum profit seen.

Time complexity: O(n)
Space complexity: O(1)
