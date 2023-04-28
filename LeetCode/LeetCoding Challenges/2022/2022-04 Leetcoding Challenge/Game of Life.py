class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        NEIGHBOURS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                liveNeighbours = 0
                for neighbour in NEIGHBOURS:
                    r, c = row + neighbour[0], col + neighbour[1]
                    if r >= 0 and r < rows and c >= 0 and c < cols and abs(board[r][c]) == 1:
                        liveNeighbours += 1
                if board[row][col] == 1 and (liveNeighbours < 2 or liveNeighbours > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and liveNeighbours == 3:
                    board[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0