class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        n, k, prevMinCost, prevMinColor, prevSecondMinCost = len(costs), len(costs[0]), None, None, None
        for color, cost in enumerate(costs[0]):
            if prevMinCost is None or cost < prevMinCost:
                prevSecondMinCost, prevMinCost, prevMinColor = prevMinCost, cost, color
            elif prevSecondMinCost is None or cost < prevSecondMinCost:
                prevSecondMinCost = cost
        for house in range(1, n):
            minCost = secondMinCost = minColor = None
            for color in range(k):
                cost = costs[house][color]
                if color == prevMinColor:
                    cost += prevSecondMinCost
                else:
                    cost += prevMinCost
                if minCost is None or cost < minCost:
                    secondMinCost, minCost, minColor = minCost, cost, color
                elif secondMinCost is None or cost < secondMinCost:
                    secondMinCost = cost
            prevMinCost, prevMinColor, prevSecondMinCost = minCost, minColor, secondMinCost
        return prevMinCost