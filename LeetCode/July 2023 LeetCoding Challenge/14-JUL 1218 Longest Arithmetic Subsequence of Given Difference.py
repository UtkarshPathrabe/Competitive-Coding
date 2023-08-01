class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        result = 1
        for num in arr:
            beforeNum = dp[num - difference]
            dp[num] = beforeNum + 1
            result = max(result, dp[num])
        return result