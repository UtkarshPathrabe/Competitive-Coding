class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return sorted(set(permutations(nums)))