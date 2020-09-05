class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        result = 0
        neighbours = defaultdict(set)
        directedEdge = defaultdict(set)
        for From, To in connections:
            directedEdge[From].add(To)
            neighbours[From].add(To)
            neighbours[To].add(From)
        seen = set()
        
        def dfs(city):
            nonlocal result
            for neighbour in neighbours[city]:
                if neighbour not in seen:
                    seen.add(city)
                    if city not in directedEdge[neighbour]:
                        result += 1
                    dfs(neighbour)
                    
        dfs(0)
        return result