class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        def checkBit(num, i):
            return (num >> i) & 1 == 1          # return positive value as is
        for i in range(32):
            bitCount = 0
            for num in nums:
                if checkBit(num, i):
                    bitCount += 1
            if bitCount % 3 == 1:
                result |= (1 << i)
        return result - 2 * (result & (1<<31))