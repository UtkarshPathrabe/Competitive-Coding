class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols, maxSqLen, prev = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0, 0, 0
        dp = [0] * (cols + 1)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(prev, dp[j], dp[j - 1]) + 1
                    maxSqLen = max(maxSqLen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxSqLen * maxSqLen