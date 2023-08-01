class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Length, word2Length = len(word1), len(word2)
        editDistance = [[0] * (word2Length + 1) for _ in range(word1Length + 1)]
        for i in range(word1Length + 1):
            editDistance[i][0] = i
        for i in range(word2Length + 1):
            editDistance[0][i] = i
        for i in range(1, word1Length + 1):
            for j in range(1, word2Length + 1):
                left = editDistance[i - 1][j] + 1
                down = editDistance[i][j - 1] + 1
                leftDown = editDistance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    leftDown += 1
                editDistance[i][j] = min(left, down, leftDown)
        return editDistance[word1Length][word2Length]