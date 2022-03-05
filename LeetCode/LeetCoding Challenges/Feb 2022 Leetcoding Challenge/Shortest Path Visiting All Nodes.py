class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        n, steps = len(graph), 0
        endingMask, queue = (1 << n) - 1, [(node, 1 << node) for node in range(n)]
        seen = set(queue)
        while queue:
            nextQueue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbour in graph[node]:
                    nextMask = mask | 1 << neighbour
                    if nextMask == endingMask:
                        return  1 + steps
                    if (neighbour, nextMask) not in seen:
                        seen.add((neighbour, nextMask))
                        nextQueue.append((neighbour, nextMask))
            steps += 1
            queue = nextQueue