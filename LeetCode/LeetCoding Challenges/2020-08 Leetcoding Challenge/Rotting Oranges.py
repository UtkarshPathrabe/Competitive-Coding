class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROTTEN_ORANGE = 2
        FRESH_ORANGE = 1
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        numberOfRows, numberOfColumns = len(grid), len(grid[0])
        freshOranges = 0
        for rowNumber in range(numberOfRows):
            for columnNumber in range(numberOfColumns):
                if grid[rowNumber][columnNumber] == ROTTEN_ORANGE:
                    queue.append((rowNumber, columnNumber))
                elif grid[rowNumber][columnNumber] == FRESH_ORANGE:
                    freshOranges += 1
        queue.append((-1, -1))
        minutesElapsed = -1
        while queue:
            rowNumber, columnNumber = queue.popleft()
            if rowNumber == -1:
                minutesElapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for direction in DIRECTIONS:
                    neighbourRow, neighbourColumn = rowNumber + direction[0], columnNumber + direction[1]
                    if numberOfRows > neighbourRow >= 0 and numberOfColumns > neighbourColumn >= 0:
                        if grid[neighbourRow][neighbourColumn] == FRESH_ORANGE:
                            grid[neighbourRow][neighbourColumn] = ROTTEN_ORANGE
                            freshOranges -= 1
                            queue.append((neighbourRow, neighbourColumn))
        return minutesElapsed if freshOranges == 0 else -1