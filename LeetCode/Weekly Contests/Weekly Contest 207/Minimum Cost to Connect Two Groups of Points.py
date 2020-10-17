class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        g1Size, g2Size = len(cost), len(cost[0])
        g2Mins = [min(cost[i][j] for i in range(g1Size)) for j in range(g2Size)]
        @lru_cache(None)
        def dfs(g1Index, group2):
            sumCost = 0 if g1Index >= g1Size else float('inf')
            if g1Index >= g1Size:
                for i in range(g2Size):
                    if group2 & (1 << i) == 0:
                        sumCost += g2Mins[i]
            else:
                for i in range(g2Size):
                    sumCost = min(sumCost, cost[g1Index][i] + dfs(g1Index + 1, group2 | (1 << i)))
            return sumCost
        return dfs(0, 0)