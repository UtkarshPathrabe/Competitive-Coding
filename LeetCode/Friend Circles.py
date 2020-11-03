class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited, count = [0] * len(M), 0
        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(i)
                count += 1
        return count