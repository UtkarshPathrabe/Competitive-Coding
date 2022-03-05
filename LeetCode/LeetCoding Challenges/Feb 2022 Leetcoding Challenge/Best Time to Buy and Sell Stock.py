class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minCost = 0, float('inf')
        for price in prices:
            minCost = min(minCost, price)
            maxProfit = max(maxProfit, price - minCost)
        return maxProfit