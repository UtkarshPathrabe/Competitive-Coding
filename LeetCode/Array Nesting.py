class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if nums[i] != -1:
                start, count = nums[i], 0
                while nums[start] != -1:
                    temp = start
                    start = nums[start]
                    count += 1
                    nums[temp] = -1
                result = max(result, count)
        return result