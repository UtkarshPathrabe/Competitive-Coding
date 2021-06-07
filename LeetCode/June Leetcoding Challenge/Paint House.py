class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        costsLength = len(costs)
        if costsLength == 0:
            return 0
        prevRow = costs[-1]
        for i in range(costsLength - 2, -1, -1):
            currRow = list(costs[i])
            currRowLength = len(currRow)
            for j in range(currRowLength):
                currRow[j] += min([prevRow[k] for k in range(currRowLength) if k != j])
            prevRow = currRow
        return min(prevRow)