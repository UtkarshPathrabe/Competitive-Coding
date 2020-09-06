class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        result = previous = 0
        for i in range(1, len(s)):
            if s[previous] != s[i]:
                previous = i
            else:
                result += min(cost[previous], cost[i])
                if cost[previous] < cost[i]:
                    previous = i
        return result