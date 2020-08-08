class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumMap = defaultdict(int)
        sumMap[0] = -1
        currentSum = 0
        for i, num in enumerate(nums):
            currentSum += num
            if k != 0:
                currentSum %= k
            if currentSum in sumMap:
                if i - sumMap[currentSum] >= 2:
                    return True
            else:
                sumMap[currentSum] = i
        return False