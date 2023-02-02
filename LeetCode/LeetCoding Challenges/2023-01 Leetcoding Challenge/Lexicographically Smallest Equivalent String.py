class UnionFind:
    def __init__(self):
        self._parent = defaultdict(str)
        for char in string.ascii_lowercase[:26]:
            self._parent[char] = char
    
    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if rootX < rootY:
            self._parent[rootY] = rootX
        else:
            self._parent[rootX] = rootY

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        disjointSet = UnionFind()
        for char1, char2 in zip(s1, s2):
            disjointSet.union(char1, char2)
        result = []
        for char in baseStr:
            result.append(disjointSet.find(char))
        return ''.join(result)