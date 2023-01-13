class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        def checkBit(num, i):
            return (num >> i) & 1 == 1
        pos = -1
        for i in range(32):
            if checkBit(xor, i):
                pos = i
                break
        s1, s2 = 0, 0
        for num in nums:
            if checkBit(num, pos):
                s1 ^= num
            else:
                s2 ^= num
        return [s1, s2]