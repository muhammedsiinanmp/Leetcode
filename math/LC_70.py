class Solution:
    def climbStairs(self, n: int) -> int:
        """Compute number of distinct ways to climb n stairs taking 1 or 2 steps.

        Iterative DP (fibonacci-like): ways[0]=1, ways[1]=1, and ways[i]=ways[i-1]+ways[i-2].
        Time: O(n), Space: O(1) using two variables.
        """
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
