class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for combSum in range(target + 1):
            for num in nums:
                if combSum - num >= 0:
                    dp[combSum] += dp[combSum - num]
                else:
                    break
        return dp[target]