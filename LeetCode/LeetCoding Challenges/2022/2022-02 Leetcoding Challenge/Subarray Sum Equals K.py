class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        countOfSubArrays = 0
        subArraySum = 0
        sumMap[0] = 1
        for n in nums:
            subArraySum += n
            if sumMap.get(subArraySum - k) is not None:
                countOfSubArrays += sumMap.get(subArraySum - k)
            sumMap[subArraySum] += 1
        return countOfSubArrays