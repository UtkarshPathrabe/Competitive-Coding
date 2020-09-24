class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        colors, availableColors, graph = [None] * N, [1, 2, 3, 4], defaultdict(set)
        for path in paths:
            graph[path[0]].add(path[1])
            graph[path[1]].add(path[0])
        for garden in range(1, N + 1):
            usedColors = set([colors[adjacent - 1] for adjacent in graph[garden]])
            for color in availableColors:
                if color not in usedColors:
                    colors[garden - 1] = color
                    break
        return colors