class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        VISITED_FLAG = '#'
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        wordLen = len(word)
        if wordLen == 0:
            return True
        if rows == 0 or cols == 0:
            return False
        result = False
        
        def backtrack(row, col, index):
            nonlocal result
            if result:
                return
            if wordLen == index:
                result = True
                return
            char = board[row][col]
            board[row][col] = VISITED_FLAG
            for direction in DIRECTIONS:
                newRow, newCol = row + direction[0], col + direction[1]
                if not result and newRow >= 0 and newCol >= 0 and newRow < rows and newCol < cols and board[newRow][newCol] == word[index]:
                    backtrack(newRow, newCol, index + 1)
            board[row][col] = char
        
        for row in range(rows):
            for col in range(cols):
                if result:
                    break
                if board[row][col] == word[0]:
                    backtrack(row, col, 1)
        return result