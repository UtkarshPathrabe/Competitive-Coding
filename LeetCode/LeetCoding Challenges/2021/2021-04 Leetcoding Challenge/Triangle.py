class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        dp, n = triangle[-1][:], len(triangle)
        if n == 1:
            return triangle[0][0]
        for row in range(n - 2, -1, -1):
            for col in range(row + 1):
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]
        return dp[0]