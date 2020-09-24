class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(counterMap):
            currentSum = 0
            for char in counterMap:
                if counterMap[char] > 0:
                    currentSum += 1
                    counterMap[char] -= 1
                    currentSum += dfs(counterMap)
                    counterMap[char] += 1
            return currentSum
        return dfs(Counter(tiles))