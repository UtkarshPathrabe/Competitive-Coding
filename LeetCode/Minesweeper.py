class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col, rows, cols = click[0], click[1], len(board), len(board[0])
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        adjacentMinesCount = 0
        for dirx, diry in DIRECTIONS:
            newRow, newCol = row + dirx, col + diry
            if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] == 'M':
                adjacentMinesCount += 1
        if adjacentMinesCount > 0:
            board[row][col] = str(adjacentMinesCount)
            return board
        board[row][col] = 'B'
        for dirx, diry in DIRECTIONS:
            newRow, newCol = row + dirx, col + diry
            if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] == 'E':
                board = self.updateBoard(board, [newRow, newCol])
        return board