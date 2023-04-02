class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        subsetSum = totalSum // 2
        dp = [[None] * (subsetSum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        def helper(n, currentSum):
            if currentSum == 0:
                return True
            if currentSum < 0 or n == 0:
                return False
            if dp[n][currentSum] != None:
                return dp[n][currentSum]
            result = helper(n - 1, currentSum) or helper(n - 1, currentSum - nums[n])
            dp[n][currentSum] = result
            return result
        return helper(len(nums) - 1, subsetSum)