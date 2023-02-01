class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        minNumber, maxNumber = nums[0], nums[0]
        for i in range(1, len(nums)):
            minNumber = min(minNumber, nums[i])
            maxNumber = max(maxNumber, nums[i])
        return gcd(minNumber, maxNumber)