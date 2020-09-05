class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positiveNumbers, negativeNumbers, maxLength = 0, 0, 0
        for num in nums:
            if num == 0:
                positiveNumbers, negativeNumbers = 0, 0
            elif num > 0:
                positiveNumbers += 1
                if negativeNumbers != 0:
                    negativeNumbers += 1
                maxLength = max(maxLength, positiveNumbers)
            else:
                positiveNumbers, negativeNumbers = negativeNumbers, positiveNumbers
                negativeNumbers += 1
                if positiveNumbers != 0:
                    positiveNumbers += 1
                maxLength = max(maxLength, positiveNumbers)
        return maxLength