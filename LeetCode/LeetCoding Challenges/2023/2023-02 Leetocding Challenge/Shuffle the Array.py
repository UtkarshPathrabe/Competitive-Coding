class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [float('-inf')] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]
            result[(2 * i) + 1] = nums[n + i]
        return result