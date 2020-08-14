class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maximumProfit += (prices[i] - prices[i - 1])
        return maximumProfit