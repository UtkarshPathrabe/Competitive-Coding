class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l = [col for row in grid for col in row] # grid to list
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        l = l[-k:] + l[:-k] # shift k times
        return [l[i * n: i * n + n] for i in range(m)]  # list to grid