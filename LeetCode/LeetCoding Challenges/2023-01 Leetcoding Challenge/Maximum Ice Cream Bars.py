class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        for cost in costs:
            if cost <= coins:
                result += 1
                coins -= cost
            else:
                break
        return result