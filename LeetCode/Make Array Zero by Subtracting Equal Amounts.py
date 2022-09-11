class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashSet = set(nums)
        return len(hashSet) - 1 if 0 in hashSet else len(hashSet)