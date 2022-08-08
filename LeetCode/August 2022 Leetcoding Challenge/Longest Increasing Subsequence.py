class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        currentLength = 0
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, currentLength)
            dp[i] = num
            if i == currentLength:
                currentLength += 1
        return currentLength