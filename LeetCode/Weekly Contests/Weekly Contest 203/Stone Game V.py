class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        
        @lru_cache(None)
        def playGame(start, end):
            if end - start <= 1:
                return 0
            if dp[start][end] == -1:
                for mid in range(start + 1, end):
                    leftSum = sum(stoneValue[start: mid])
                    rightSum = sum(stoneValue[mid: end])
                    if leftSum <= rightSum:
                        dp[start][end] = max(dp[start][end], leftSum + playGame(start, mid))
                    if leftSum >= rightSum:
                        dp[start][end] = max(dp[start][end], rightSum + playGame(mid, end))
            return dp[start][end]
        
        return playGame(0, n)