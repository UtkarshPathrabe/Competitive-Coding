class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        numberOfRows = len(maze)
        if numberOfRows == 0:
            return False
        numberOfColumns = len(maze[0])
        visited = [[False] * numberOfColumns for _ in range(numberOfRows)]
        
        def dfs(maze: List[List[int]], start: List[int], destination: List[int], visited: List[List[int]]) -> bool:
            if visited[start[0]][start[1]]:
                return False
            if start[0] == destination[0] and start[1] == destination[1]:
                return True
            visited[start[0]][start[1]] = True
            right, left, up, down = start[1] + 1, start[1] - 1, start[0] - 1, start[0] + 1
            while right < numberOfColumns and maze[start[0]][right] == 0:
                right += 1
            if dfs(maze, [start[0], right - 1], destination, visited):
                return True
            while left >= 0 and maze[start[0]][left] == 0:
                left -= 1
            if dfs(maze, [start[0], left + 1], destination, visited):
                return True
            while up >= 0 and maze[up][start[1]] == 0:
                up -= 1
            if dfs(maze, [up + 1, start[1]], destination, visited):
                return True
            while down < numberOfRows and maze[down][start[1]] == 0:
                down += 1
            if dfs(maze, [down - 1, start[1]], destination, visited):
                return True
            return False
        
        return dfs(maze, start, destination, visited)