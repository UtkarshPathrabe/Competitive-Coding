class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        
        def findParent(x):
            if parent[x] != x:
                parent[x] = findParent(parent[x])
            return parent[x]
        
        def unionPossible(x, y):
            px, py = findParent(x), findParent(y)
            if px == py:
                return False
            else:
                parent[px] = py
                return True
        
        result = edgesForAlice = edgesForBob = 0
        for Type, From, To in edges:
            if Type == 3:
                if unionPossible(From, To):
                    edgesForAlice += 1
                    edgesForBob += 1
                else:
                    result += 1
        parentCopy = copy.copy(parent)
        for Type, From, To in edges:
            if Type == 1:
                if unionPossible(From, To):
                    edgesForAlice += 1
                else:
                    result += 1
        parent = copy.copy(parentCopy)
        for Type, From, To in edges:
            if Type == 2:
                if unionPossible(From, To):
                    edgesForBob += 1
                else:
                    result += 1
        return result if edgesForAlice == edgesForBob == n - 1 else -1