class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            mid = start + ((end - start) >> 1)
            currentSum = (mid * (mid + 1)) >> 1
            if currentSum == n:
                return mid
            elif currentSum > n:
                end = mid - 1
            else:
                start = mid + 1
        return end