class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S, K, dp = str(n), len(str(n)), [0] * len(str(n)) + [1]
        for i in range(K - 1, -1, -1):
            for d in digits:
                if d < S[i]:
                    dp[i] += len(digits) ** (K - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i + 1]
        return dp[0] + sum(len(digits) ** i for i in range(1, K))