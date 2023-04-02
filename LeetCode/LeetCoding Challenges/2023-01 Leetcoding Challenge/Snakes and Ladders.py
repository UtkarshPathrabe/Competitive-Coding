class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label, columns = 1, list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        distance = [-1] * (n**2 + 1)
        queue = deque([1])
        distance[1] = 0
        while queue:
            current = queue.popleft()
            for neighbour in range(current + 1, min(current + 6, n**2) + 1):
                row, column = cells[neighbour]
                destination = (board[row][column] if board[row][column] != -1 else neighbour)
                if distance[destination] == -1:
                    distance[destination] = distance[current] + 1
                    queue.append(destination)
        return distance[n * n]