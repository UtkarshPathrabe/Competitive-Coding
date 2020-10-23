class Solution:
    def minOperations(self, nums: List[int]) -> int:
        evenMax, totalOdd = 0, 0
        for num in nums:
            even, odd, n = 0, 0, num
            while n > 0:
                if n % 2 == 1:
                    odd += 1
                    n -= 1
                else:
                    even += 1
                    n = n // 2
            evenMax = max(evenMax, even)
            totalOdd += odd
        return evenMax + totalOdd