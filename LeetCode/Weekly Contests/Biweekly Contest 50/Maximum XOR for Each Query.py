class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result, dp = [0] * len(nums), [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] ^ nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[len(nums) - 1 - i] = dp[i] ^ (pow(2, maximumBit) - 1)
        return result