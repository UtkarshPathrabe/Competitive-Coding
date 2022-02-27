class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, totalTank, currentTank, startStation = len(gas), 0, 0, 0
        for i in range(n):
            totalTank += gas[i] - cost[i]
            currentTank += gas[i] - cost[i]
            if currentTank < 0:
                startStation = i + 1
                currentTank = 0
        return startStation if totalTank >= 0 else -1