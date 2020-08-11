class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        self.EMPTY = 2147483647
        self.GATE = 0
        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        numberOfRows = len(rooms)
        if numberOfRows == 0:
            return
        numberOfColumns = len(rooms[0])
        queue = deque()
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if rooms[row][column] == self.GATE:
                    queue.append((row, column))
        while queue:
            row, column = queue.popleft()
            for rowDirection, columnDirection in self.DIRECTIONS:
                r = row + rowDirection
                c = column + columnDirection
                if r < 0 or c < 0 or r >= numberOfRows or c >= numberOfColumns or rooms[r][c] != self.EMPTY:
                    continue
                rooms[r][c] = rooms[row][column] + 1
                queue.append((r, c))