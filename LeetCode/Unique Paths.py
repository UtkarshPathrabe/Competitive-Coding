class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                paths[row][col] = paths[row-1][col] + paths[row][col-1]
        return paths[m-1][n-1]