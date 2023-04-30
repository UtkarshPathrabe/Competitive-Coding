class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        END_FLAG, VISITED_FLAG = '$', '#'
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matchedWords = []
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        if rows == 0 or cols == 0:
            return matchedWords
        trie = {}
        for word in words:
            currentNode = trie
            for char in word:
                currentNode = currentNode.setdefault(char, {})
            currentNode[END_FLAG] = word
        
        def backtrack(row, col, parentNode):
            char = board[row][col]
            currentNode = parentNode[char]
            wordMatch = currentNode.pop(END_FLAG, False)
            if wordMatch:
                matchedWords.append(wordMatch)
            board[row][col] = VISITED_FLAG
            for direction in DIRECTIONS:
                newRow, newCol = row + direction[0], col + direction[1]
                if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and board[newRow][newCol] in currentNode:
                    backtrack(newRow, newCol, currentNode)
            board[row][col] = char
            if not currentNode:
                parentNode.pop(char)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    backtrack(row, col, trie)
        return matchedWords