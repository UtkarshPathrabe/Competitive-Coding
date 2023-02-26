class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD, N = 10**9 + 7, len(arr)
        arr.sort()
        dp, index = [1] * N, {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    right = x // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD