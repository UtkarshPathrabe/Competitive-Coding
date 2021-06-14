class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        distance = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        def dijkstra(start: List[int], distance: List[List[int]]):
            DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            heap = [(0, start[0], start[1])]
            while heap:
                s = heapq.heappop(heap)
                if distance[s[1]][s[2]] < s[0]:
                    continue
                for d in DIRECTIONS:
                    x, y, count = s[1] + d[0], s[2] + d[1], 0
                    while x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 0:
                        x, y, count = x + d[0], y + d[1], count + 1
                    if distance[s[1]][s[2]] + count < distance[x - d[0]][y - d[1]]:
                        distance[x - d[0]][y - d[1]] = distance[s[1]][s[2]] + count
                        heapq.heappush(heap, (distance[x - d[0]][y - d[1]], x - d[0], y - d[1]))
        dijkstra(start, distance)
        return -1 if distance[destination[0]][destination[1]] == float('inf') else distance[destination[0]][destination[1]]