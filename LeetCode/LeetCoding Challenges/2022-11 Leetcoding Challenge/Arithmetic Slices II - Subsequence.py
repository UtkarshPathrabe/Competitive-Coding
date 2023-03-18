class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # use defaultdict(int) to easily get the difference in arithmetic subsequences ending with ```j```
        dp = [defaultdict(int) for _ in range(len(nums))]
        result = 0
        for i in range(len(nums)):
            for j in range(i):
                # We are looking for the number of elements before j in the arithmetic subsequence that has nums[j]-nums[i] as difference.
                diff = nums[j] - nums[i]
                # Simply add it to the result.
                result += dp[j][diff]
                # Increase the number of elements in arithmetic subsequence at i with this dif.
                dp[i][diff] += dp[j][diff] + 1
        return result