class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # Sort integers by values.
        numsAndCosts = sorted([num, cost] for num, cost in zip(nums, costs))
        n = len(costs)
        # Get the prefix sum array of the costs.
        prefixCost = [0] * n
        prefixCost[0] = numsAndCosts[0][1]
        for i in range(1, n): 
            prefixCost[i] = numsAndCosts[i][1] + prefixCost[i - 1]
        # Then we try every integer nums[i] and make every element equals nums[i],
        # Start with nums[0]
        totalCost = 0
        for i in range(1, n):
            totalCost += numsAndCosts[i][1] * (numsAndCosts[i][0] - numsAndCosts[0][0])
        result = totalCost
        # Then we try nums[1], nums[2] and so on. The cost difference is made by the change of
        # two parts: 1. prefix sum of costs. 2. suffix sum of costs. 
        # During the iteration, record the minimum cost we have met.
        for i in range(1, n):
            gap = numsAndCosts[i][0] - numsAndCosts[i - 1][0]
            totalCost += prefixCost[i - 1] * gap
            totalCost -= gap * (prefixCost[n - 1] - prefixCost[i - 1])
            result = min(result, totalCost)
        return result