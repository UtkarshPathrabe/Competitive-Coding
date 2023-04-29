class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)
        dp = [0] * (m + 1)
        for op in range(m - 1, -1, -1):
            nextRow = dp.copy()
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + nextRow[left + 1],
                              multipliers[op] * nums[n - 1 - (op - left)] + nextRow[left])
        return dp[0]