class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(set)
        longestPath = 1
        for i in range(1, len(parent)):
            graph[parent[i]].add(i)
        def dfs(node):
            nonlocal longestPath
            # if node is a leaf node
            if node not in graph:
                return 1
            longestChain, secondLongestChain = 0, 0
            for child in graph[node]:
                longestChainStartingFromChild = dfs(child)
                # if chracters are same at both parent and child, ignore
                if s[node] == s[child]:
                    continue
                if longestChainStartingFromChild > longestChain:
                    secondLongestChain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestChain:
                    secondLongestChain = longestChainStartingFromChild
            longestPath = max(longestPath, 1 + longestChain + secondLongestChain)
            return 1 + longestChain
        dfs(0)
        return longestPath