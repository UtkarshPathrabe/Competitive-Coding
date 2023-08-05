class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from node i to node j, if bomb i denotes bomb j
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
        
        # DFS to get the number of nodes reachable from a given node curr
        def dfs(curr, visited):
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
            return len(visited)
        
        result = 0
        for i in range(n):
            visited = set()
            result = max(result, dfs(i, visited))
        return result