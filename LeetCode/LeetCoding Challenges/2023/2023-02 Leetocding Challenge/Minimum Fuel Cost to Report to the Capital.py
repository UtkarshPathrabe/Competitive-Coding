class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])

        self.fuel = 0

        def dfs(node, parent, adj, seats):
            representatives = 1
            for child in adj[node]:
                if child != parent:
                    representatives += dfs(child, node, adj, seats)
            if node != 0:
                self.fuel += math.ceil(representatives / seats)
            return representatives

        dfs(0, -1, adj, seats)
        return self.fuel