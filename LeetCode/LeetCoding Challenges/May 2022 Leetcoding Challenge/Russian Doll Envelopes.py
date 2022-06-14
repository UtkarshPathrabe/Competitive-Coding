class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        def LIS(nums):
            dp = []
            for num in nums:
                index = bisect.bisect_left(dp, num)
                if index == len(dp):
                    dp.append(num)
                else:
                    dp[index] = num
            return len(dp)
        return LIS([x[1] for x in envelopes])