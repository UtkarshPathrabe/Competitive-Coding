class UnionFind:
    def __init__(self, size: int):
        self.group = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def union(self, nodeA: int, nodeB: int):
        groupA, groupB = self.find(nodeA), self.find(nodeB)
        # node1 and node2 already belong to same group.
        if groupA == groupB:
            return
        if self.rank[groupA] > self.rank[groupB]:
            self.group[groupB] = groupA
        elif self.rank[groupA] < self.rank[groupB]:
            self.group[groupA] = groupB
        else:
            self.group[groupA] = groupB
            self.rank[groupB] += 1
    
    def areConnected(self, nodeA: int, nodeB: int) -> bool:
        return self.find(nodeA) == self.find(nodeB)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        queriesCount = len(queries)
        answer = [False] * queriesCount
        # Store original indices with all queries.
        queriesWithIndex = []
        for i in range(queriesCount):
            queriesWithIndex.append((queries[i][0], queries[i][1], queries[i][2], i))
        # Sort all edges in increasing order of their edge weights.
        edgeList.sort(key=lambda x: x[2])
        # Sort all queries in increasing order of the limit of edge allowed.
        queriesWithIndex.sort(key=lambda x: x[2])
        edgeIndex = 0
        # Iterate on each query one by one
        for [p, q, limit, queryOriginalIndex] in queriesWithIndex:
            # We can attach all edges which satisfy the limit given by the query.
            while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
                uf.union(edgeList[edgeIndex][0], edgeList[edgeIndex][1])
                edgeIndex += 1
            # If both nodes belong to the same component, it means we can reach them. 
            answer[queryOriginalIndex] = uf.areConnected(p, q)
        return answer