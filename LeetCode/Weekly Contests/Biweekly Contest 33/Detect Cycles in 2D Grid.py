class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols, visited, directions = len(grid), len(grid[0]), set(), [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(row, col, parentX, parentY, length):
            visited.add((row, col))
            for dirX, dirY in directions:
                newRow, newCol = row + dirX, col + dirY
                if newRow < 0 or newCol < 0 or newRow >= rows or newCol >= cols or (parentX == newRow and parentY == newCol):
                    continue
                if (newRow, newCol) in visited and length >= 4 and grid[row][col] == grid[newRow][newCol]:
                    return True
                elif grid[row][col] == grid[newRow][newCol]:
                    if dfs(newRow, newCol, row, col, length + 1):
                        return True
            return False
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                if dfs(row, col, None, None, 1):
                    return True
        return False