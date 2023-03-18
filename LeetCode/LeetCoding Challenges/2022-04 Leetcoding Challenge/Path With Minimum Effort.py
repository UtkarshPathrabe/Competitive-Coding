class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0], heap = 0, [(0, 0, 0)]
        while heap:
            distance, row, col = heappop(heap)
            if row == rows - 1 and col == cols - 1:
                return distance
            if distance > dist[row][col]:
                continue
            for r, c in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols:
                    tempDistance = max(distance, abs(heights[row][col] - heights[r][c]))
                    if tempDistance < dist[r][c]:
                        dist[r][c] = tempDistance
                        heappush(heap, (tempDistance, r, c))