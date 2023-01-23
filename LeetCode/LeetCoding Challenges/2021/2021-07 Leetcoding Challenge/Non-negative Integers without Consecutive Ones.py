class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 32
        dp[0], dp[1] = 1, 2
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        i, currentSum, prevBit = 30, 0, 0
        while i >= 0:
            if (n & (1 << i)) != 0:
                currentSum += dp[i]
                if prevBit == 1:
                    currentSum -= 1
                    break
                prevBit = 1
            else:
                prevBit = 0
            i -= 1
        return currentSum + 1