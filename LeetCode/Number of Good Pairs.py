class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(((freq * (freq - 1)) // 2) for _, freq in Counter(nums).items())