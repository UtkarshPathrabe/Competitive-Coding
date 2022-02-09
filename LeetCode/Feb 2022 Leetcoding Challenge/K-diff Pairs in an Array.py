class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result, frequencyMap = 0, Counter(nums)
        for i in frequencyMap:
            if k == 0 and frequencyMap[i] > 1:
                result += 1
            elif k > 0 and i + k in frequencyMap:
                result += 1
        return result