class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        discoveryTime = [-1 for _ in range(n)]
        lowTime = [-1 for _ in range(n)]
        seen = [False for _ in range(n)]
        time, result = 0, []
        
        def dfs(node, parent = None):
            nonlocal time
            discoveryTime[node] = time
            lowTime[node] = time
            seen[node] = True
            time += 1
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if seen[neighbour]:
                    lowTime[node] = min(lowTime[node], discoveryTime[neighbour])
                else:
                    dfs(neighbour, node)
                    lowTime[node] = min(lowTime[node], lowTime[neighbour])
                    if lowTime[neighbour] > discoveryTime[node]:
                        result.append([node, neighbour])
        
        for i in range(n):
            if not seen[i]:
                dfs(i)
        return result