class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result, currentRange = [], []
        for num in nums:
            if len(currentRange) == 0:
                currentRange = [num, num]
            elif len(currentRange) == 2:
                if currentRange[-1] + 1 == num:
                    currentRange[-1] = num
                else:
                    result.append(currentRange)
                    currentRange = [num, num]
        if len(currentRange) == 2:
            result.append(currentRange)
        return [str(x[0]) + '->' + str(x[1]) if x[0] != x[1] else str(x[0]) for x in result]