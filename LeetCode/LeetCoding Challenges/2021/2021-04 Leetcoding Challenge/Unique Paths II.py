class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        numberOfRows = len(obstacleGrid)
        numberOfColumns = len(obstacleGrid[0])
        for col in range(1, numberOfColumns):
            if obstacleGrid[0][col] == 1:
                obstacleGrid[0][col] = 0
            else:
                obstacleGrid[0][col] = obstacleGrid[0][col - 1]
        for row in range(1, numberOfRows):
            if obstacleGrid[row][0] == 1:
                obstacleGrid[row][0] = 0
            else:
                obstacleGrid[row][0] = obstacleGrid[row - 1][0]
        for row in range(1, numberOfRows):
            for col in range(1, numberOfColumns):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
        return obstacleGrid[numberOfRows - 1][numberOfColumns - 1]