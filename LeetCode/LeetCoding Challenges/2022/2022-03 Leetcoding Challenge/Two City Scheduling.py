class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs, L = sorted(costs, key = lambda a: a[0] - a[1]), len(costs) // 2
        return sum(c[0] for c in costs[:L]) + sum(c[1] for c in costs[L:])