class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[0], cost[1], 0]
        for i in range(2, n):
            dp[i % 3] = cost[i] + min(dp[(i - 1) % 3], dp[(i - 2) % 3])
        return min(dp[(n - 1) % 3], dp[(n - 2) % 3])