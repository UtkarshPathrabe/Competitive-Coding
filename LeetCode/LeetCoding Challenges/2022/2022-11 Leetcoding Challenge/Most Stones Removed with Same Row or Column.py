class DisjointSet:
    
    def __init__(self):
        self.parent = list(range(20000))
        self.rank = [0] * 20000
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xParent, yParent = self.find(x), self.find(y)
        if xParent == yParent:
            return
        elif self.rank[xParent] < self.rank[yParent]:
            self.parent[xParent] = yParent
        elif self.rank[xParent] > self.rank[yParent]:
            self.parent[yParent] = xParent
        else:
            self.parent[yParent] = xParent
            self.rank[xParent] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        disjointSet = DisjointSet()
        for x, y in stones:
            disjointSet.union(x, y + 10000)
        return N - len({disjointSet.find(x) for x, y in stones})