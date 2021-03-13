class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # dp[p][k] = probability of obtaining k heads for first p coins
        dp = [[0] * (target + 1) for _ in range(len(prob) + 1)]
        dp[0][0] = 1
        for p in range(1, len(prob) + 1):
            dp[p][0] = dp[p - 1][0] * (1 - prob[p - 1])
        for k in range(1, target + 1):
            for p in range(k, len(prob) + 1):
                dp[p][k] = (dp[p - 1][k] * (1 - prob[p - 1])) + (dp[p - 1][k - 1] * prob[p - 1])
        return dp[-1][-1]