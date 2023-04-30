class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        cache = {}
        def helper(n, currentSum):
            if n == 0 and currentSum == target:
                return 1
            if n == 0 or currentSum > target:
                return 0
            if (n, currentSum) in cache:
                return cache[(n, currentSum)]
            count = 0
            for i in range(1, k+1):
                count += helper(n-1, currentSum + i)
            cache[(n, currentSum)] = count
            return count
        return helper(n, 0) % (10**9+7)