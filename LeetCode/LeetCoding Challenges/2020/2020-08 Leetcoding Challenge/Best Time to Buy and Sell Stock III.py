class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1Cost, t1Profit, t2Cost, t2Profit = float('inf'), 0, float('inf'), 0
        for price in prices:
            t1Cost = min(t1Cost, price)
            t1Profit = max(t1Profit, price - t1Cost)
            t2Cost = min(t2Cost, price - t1Profit)
            t2Profit = max(t2Profit, price - t2Cost)
        return t2Profit