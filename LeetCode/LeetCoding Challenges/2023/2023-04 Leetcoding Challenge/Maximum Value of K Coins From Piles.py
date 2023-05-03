class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @lru_cache(None)
        def helper(i, coins):
            if i == 0:
                return 0
            currentSum, result = 0, 0
            for currentCoins in range(0, min(len(piles[i - 1]), coins) + 1):
                if currentCoins > 0:
                    currentSum += piles[i - 1][currentCoins - 1]
                result = max(result, helper(i - 1, coins - currentCoins) + currentSum)
            return result
        
        return helper(n, k)