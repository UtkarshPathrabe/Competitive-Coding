class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        length = len(nums)
        hashMap = {0: -1}
        runningSum = [0]
        for i, num in enumerate(nums):
            runningSum.append(runningSum[-1] + num)
            currentRemainder = runningSum[-1] % p
            if currentRemainder >= remainder:
                if currentRemainder - remainder in hashMap:
                    length = min(length, i - hashMap[currentRemainder - remainder])
            else:
                if p - remainder + currentRemainder in hashMap:
                    length = min(length, i - hashMap[p - remainder + currentRemainder])
            hashMap[currentRemainder] = i
        if length == len(nums):
            return -1
        return length