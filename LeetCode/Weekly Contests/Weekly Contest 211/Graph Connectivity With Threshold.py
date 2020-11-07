class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent, size, result = [i for i in range(n + 1)], [1 for _ in range(n + 1)], []
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if size[px] > size[py]:
                size[px] += size[py]
                parent[py] = px
            else:
                size[py] += size[px]
                parent[px] = py
            return True
        
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                if i > threshold:
                    union(i, j)
        for a, b in queries:
            result.append(find(a) == find(b))
        return result
                