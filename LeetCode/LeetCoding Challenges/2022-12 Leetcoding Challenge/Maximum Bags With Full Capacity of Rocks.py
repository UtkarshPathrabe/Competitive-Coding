class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffArray = [(capacity[i] - rocks[i]) for i in range(len(rocks))]
        diffArray.sort()
        result, i = 0, 0
        while additionalRocks > 0 and i < len(rocks) and diffArray[i] <= additionalRocks:
            result, additionalRocks, i = result + 1, additionalRocks - diffArray[i], i + 1
        return result