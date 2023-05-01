class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n, countOfGroups = len(strs), 0
        adj = defaultdict(set)
        visited = set()

        def dfs(node: int):
            visited.add(node)
            if node not in adj:
                return
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        def isSimilar(a: str, b: str) -> bool:
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
            return diff == 0 or diff == 2

        # Form the required graph from the given strings array.
        for i in range(n):
            for j in range(n):
                if isSimilar(strs[i], strs[j]):
                    adj[i].add(j)
                    adj[j].add(i)
        
        # Count the number of connected components
        for node in range(n):
            if node not in visited:
                dfs(node)
                countOfGroups += 1
        return countOfGroups
        