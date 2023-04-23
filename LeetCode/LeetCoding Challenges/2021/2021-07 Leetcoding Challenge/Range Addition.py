class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        dp = [0] * length
        for start, end, inc in updates:
            dp[start] += inc
            if end + 1 < length:
                dp[end + 1] -= inc
        result = [dp[0],]
        for num in dp[1:]:
            result.append(result[-1] + num)
        return result