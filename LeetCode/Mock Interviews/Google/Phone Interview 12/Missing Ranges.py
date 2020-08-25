class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        nums.append(upper + 1)
        current = lower - 1
        for num in nums:
            if num == current + 2:
                result.append(str(num - 1))
            elif num > current + 2:
                result.append(str(current + 1) + '->' + str(num - 1))
            current = num
        return result