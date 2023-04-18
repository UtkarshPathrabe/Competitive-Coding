class DisjointSet:
    
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xParent, yParent = self.find(x), self.find(y)
        if xParent == yParent:
            return False
        elif self.rank[xParent] < self.rank[yParent]:
            self.parent[xParent] = yParent
        elif self.rank[xParent] > self.rank[yParent]:
            self.parent[yParent] = xParent
        else:
            self.parent[yParent] = xParent
            self.rank[xParent] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numberOfEdges = len(edges)
        disjointSet = DisjointSet(numberOfEdges + 1)
        for edge in edges:
            if not disjointSet.union(*edge):
                return edge