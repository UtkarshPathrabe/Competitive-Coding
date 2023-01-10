class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        missing = duplicate = -1
        for i in range(1, len(nums) + 1):
            if i in hashMap:
                if hashMap[i] == 2:
                    duplicate = i
            else:
                missing = i
        return [duplicate, missing]