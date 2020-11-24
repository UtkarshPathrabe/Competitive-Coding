class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        low, high, diffList = 0, 0, []
        for price in prices:
            price = float(price)
            f, c = math.floor(price), math.ceil(price)
            low, high = low + f, high + c
            if f != c:
                diffList.append((c - price, price - f))
        if target < low or target > high:
            return '-1'
        diffList.sort(key = lambda x:x[0])
        flipsRequired = target - int(low)
        return '{:.3f}'.format(sum(cost[0] for cost in diffList[:flipsRequired]) + sum(cost[1] for cost in diffList[flipsRequired:]))