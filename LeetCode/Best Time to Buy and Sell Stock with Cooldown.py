class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0
        for price in prices:
            sold, held, reset = held + price, max(held, reset - price), max(reset, sold)
        return max(sold, reset)