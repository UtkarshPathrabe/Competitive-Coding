class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols, color = len(image), len(image[0]), image[sr][sc]
        if color == newColor:
            return image
        def dfs(row, col):
            if image[row][col] == color:
                image[row][col] = newColor
                if row - 1 >= 0:
                    dfs(row - 1, col)
                if row + 1 < rows:
                    dfs(row + 1, col)
                if col - 1 >= 0:
                    dfs(row, col - 1)
                if col + 1 < cols:
                    dfs(row, col + 1)
        dfs(sr, sc)
        return image