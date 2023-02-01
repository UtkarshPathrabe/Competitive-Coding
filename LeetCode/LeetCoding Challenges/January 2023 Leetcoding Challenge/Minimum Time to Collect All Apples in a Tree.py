class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        def dfs(node, parent):
            if node not in graph:
                return 0
            totalTime, childTime = 0, 0
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                childTime = dfs(neighbour, node)
                # childTime > 0 indicates subtree of child has apples. Since the root node of the
                # subtree does not contribute to the time, even if it has an apple, we have to check it
                # independently.
                if childTime > 0 or hasApple[neighbour]:
                    totalTime += (childTime + 2)
            return totalTime
        return dfs(0, -1)