class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for left, right in zip(l, r):
            subArray = nums[left : (right + 1)]
            if len(subArray) == 1:
                result.append(True)
                continue
            subArray.sort()
            diff, tempResult = subArray[1] - subArray[0], True
            for i in range(2, len(subArray)):
                if subArray[i] - subArray[i - 1] != diff:
                    tempResult = False
                    break
            result.append(tempResult)
        return result