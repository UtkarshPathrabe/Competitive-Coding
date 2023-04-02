from sortedcontainers import SortedDict

class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
    
    def find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if self._rank[rootX] < self._rank[rootY]:
            self._parent[rootX] = rootY
        elif self._rank[rootX] > self._rank[rootY]:
            self._parent[rootY] = rootX
        else:
            self._parent[rootY] = rootX
            self._rank[rootX] += 1

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        n = len(vals)
        valueToNodes = SortedDict()
        for i in range(n):
            currentValue = valueToNodes.get(vals[i], set())
            currentValue.add(i)
            valueToNodes.__setitem__(vals[i], currentValue)
        disjointSet = UnionFind(n)
        goodPaths = 0
        for value in valueToNodes:
            for node in valueToNodes.get(value):
                if node not in graph:
                    continue
                for neighbour in graph[node]:
                    if vals[neighbour] <= vals[node]:
                        disjointSet.union(node, neighbour)
            group = defaultdict(int)
            for node in valueToNodes.get(value):
                group[disjointSet.find(node)] += 1
            for node, size in group.items():
                goodPaths += ((size * (size + 1)) // 2)
        return goodPaths