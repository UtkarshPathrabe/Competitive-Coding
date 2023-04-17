from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sortedList, MOD, cost, size = SortedList(), 10**9 + 7, 0, len(instructions)
        for i in range(size):
            leftCost, rightCost = sortedList.bisect_left(instructions[i]), i - sortedList.bisect_right(instructions[i])
            cost += min(leftCost, rightCost)
            sortedList.add(instructions[i])
        return cost % MOD