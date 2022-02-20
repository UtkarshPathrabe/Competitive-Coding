class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, seen, heap, result = len(grid), {(0, 0)}, [(grid[0][0], 0, 0)], 0
        while heap:
            val, row, col = heappop(heap)
            result = max(result, val)
            if row == col == N - 1:
                return result
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < N and 0 <= c < N and (r, c) not in seen:
                    heappush(heap, (grid[r][c], r, c))
                    seen.add((r, c))