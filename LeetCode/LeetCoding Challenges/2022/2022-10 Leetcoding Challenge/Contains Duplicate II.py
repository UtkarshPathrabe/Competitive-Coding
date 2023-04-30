class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i, num in enumerate(nums):
            if num in hashset:
                return True
            hashset.add(num)
            if len(hashset) > k:
                hashset.remove(nums[i - k])
        return False