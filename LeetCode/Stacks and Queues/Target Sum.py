class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [0] * 2001
        dp[nums[0] + 1000] += 1
        dp[-nums[0] + 1000] += 1
        for num in nums[1:]:
            nextDP = [0] * 2001
            for s in range(-1000, 1001):
                if dp[s + 1000] > 0:
                    nextDP[s + num + 1000] += dp[s + 1000]
                    nextDP[s - num + 1000] += dp[s + 1000]
            dp = nextDP
        return 0 if S > 1000 else dp[S + 1000]