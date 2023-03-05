class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, result = 100000, 0
        for price in prices:
            if price >= buy:
                result = max(result, price - buy)
            buy = min(price, buy)
        return result