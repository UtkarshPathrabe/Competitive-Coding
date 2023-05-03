class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        result = [0] * n
        def dfs(node, parent):
            if node not in graph:
                return defaultdict(int)
            freqMap = defaultdict(int)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                neighbourMap = dfs(neighbour, node)
                for key, freq in neighbourMap.items():
                    freqMap[key] += freq
            freqMap[labels[node]] += 1
            result[node] = freqMap[labels[node]]
            return freqMap
        dfs(0, -1)
        return result