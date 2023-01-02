class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getBucketId(num, width):
            return num // width
        if t < 0 or k < 0:
            return False
        dictionary = {}
        width = t + 1
        for i, num in enumerate(nums):
            key = getBucketId(num, width)
            if key in dictionary:
                return True
            if key - 1 in dictionary and abs(num - dictionary[key - 1]) < width:
                return True
            if key + 1 in dictionary and abs(num - dictionary[key + 1]) < width:
                return True
            dictionary[key] = num
            if i >= k:
                dictionary.pop(getBucketId(nums[i - k], width))
        return False