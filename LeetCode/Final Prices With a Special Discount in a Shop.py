class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for index, price in enumerate(prices):
            discount = 0
            for i in range(index + 1, len(prices)):
                if prices[i] <= price:
                    discount = prices[i]
                    break
            result.append(price - discount)
        return result