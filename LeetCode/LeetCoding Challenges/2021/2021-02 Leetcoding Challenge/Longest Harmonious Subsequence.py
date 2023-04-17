class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result, hashMap = 0, defaultdict(int)
        for num in nums:
            hashMap[num] += 1
            if num - 1 in hashMap:
                result = max(result, hashMap[num] + hashMap[num - 1])
            if num + 1 in hashMap:
                result = max(result, hashMap[num] + hashMap[num + 1])
        return result