class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, MOD = len(grid), len(grid[0]), 10**9 + 7
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Initialize dp, 1 stands for the path made by a cell itself.
        dp = [[1] * n for _ in range(m)]
        # Sort all cells by value
        cellList = [[i, j] for i in range(m) for j in range(n)]
        cellList.sort(key = lambda x : grid[x[0]][x[1]])
        # Iterate over the sorted cells, for each cell grid[i][j]
        for i, j in cellList:
            # Check its four neighbor cells, if a neighbor cell grid[curr_i][curr_j] has a
            # larger value, increment dp[curr_i][curr_j] by dp[i][j]
            for di, dj in DIRECTIONS:
                curri, currj = i + di, j + dj
                if 0 <= curri < m and 0 <= currj < n and grid[curri][currj] > grid[i][j]:
                    dp[curri][currj] += dp[i][j]
                    dp[curri][currj] %= MOD
        # Sum over dp[i][j].
        return sum(sum(row) % MOD for row in dp) % MOD