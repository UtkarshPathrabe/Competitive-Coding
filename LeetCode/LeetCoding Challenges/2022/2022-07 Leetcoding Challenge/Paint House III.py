class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 1000001
        prevMemo = [[MAX_COST] * n for _ in range(target + 1)]
        # Initialize for house 0, neighborhood will be 1
        for color in range(1, n + 1):
            if houses[0] == color:
                # If the house has same color, no cost
                prevMemo[1][color - 1] = 0
            elif houses[0] == 0:
                # If the house is not painted, assign the corresponding cost
                prevMemo[1][color - 1] = cost[0][color - 1]
        for house in range(1, m):
            memo = [[MAX_COST] * n for _ in range(target + 1)]
            for neighborhoods in range(1, min(target, house + 1) + 1):
                for color in range(1, n + 1):
                    # If the house is already painted, and color is different
                    if houses[house] != 0 and color != houses[house]:
                        # Cannot be painted with different color
                        continue
                    currentCost = MAX_COST
                    # Iterate over all the possible color for previous house
                    for prevColor in range(1, n + 1):
                        if prevColor != color:
                            # Decrement the neighborhood as adjacent houses have different color
                            currentCost = min(currentCost, prevMemo[neighborhoods - 1][prevColor - 1])
                        else:
                            # Previous house has the same color, no change in neighborhood count
                            currentCost = min(currentCost, prevMemo[neighborhoods][color - 1])
                    # If the house is already painted cost to paint is 0
                    costToPaint = 0 if houses[house] != 0 else cost[house][color - 1]
                    memo[neighborhoods][color - 1] = currentCost + costToPaint
            # Update the table to have the current house results
            prevMemo = memo
        minCost = MAX_COST
        # Find the minimum cost with m houses and target neighborhoods
        # By comparing cost for different color for the last house
        for color in range(1, n + 1):
            minCost = min(minCost, prevMemo[target][color - 1])
        # Return -1 if the answer is MAX_COST as it implies no answer possible
        return -1 if minCost == MAX_COST else minCost