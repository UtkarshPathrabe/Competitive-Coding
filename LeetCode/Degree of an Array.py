class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        leftIndexMap, rightIndexMap, countMap = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in leftIndexMap:
                leftIndexMap[num] = i
            rightIndexMap[num] = i
            countMap[num] = countMap.get(num, 0) + 1
        result = len(nums)
        maxDegree = max(countMap.values())
        for num in countMap:
            if countMap[num] == maxDegree:
                result = min(result, rightIndexMap[num] - leftIndexMap[num] + 1)
        return result