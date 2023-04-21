class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def helper(index: int, count: int, profit: int) -> int:
            if index == len(group):
                # If profit exceeds minimum profit required; it is a profitable scheme
                return 1 if profit >= minProfit else 0
            # Ways to get a profitable scheme without this crime.
            totalWays = helper(index + 1, count, profit)
            if count + group[index] <= n:
                # Adding ways to get profitable schemes, including this crime.
                totalWays += helper(index + 1, count + group[index], min(minProfit, profit + profits[index]))
            return totalWays % MOD
        return helper(0, 0, 0)