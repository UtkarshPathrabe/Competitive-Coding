class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prevOneIndex = float('-inf')
        for i, num in enumerate(nums):
            if num == 1:
                if i - prevOneIndex - 1 < k:
                    return False
                prevOneIndex = i
        return True