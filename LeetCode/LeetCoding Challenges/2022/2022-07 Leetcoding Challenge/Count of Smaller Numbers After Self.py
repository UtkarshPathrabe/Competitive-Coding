class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        result = [0 for _ in range(numsLength)]
        cache = []
        for i in range(numsLength - 1, -1, -1):
            insertionIndex = result[i] = bisect_left(cache, nums[i])
            cache.insert(insertionIndex, nums[i])
        return result