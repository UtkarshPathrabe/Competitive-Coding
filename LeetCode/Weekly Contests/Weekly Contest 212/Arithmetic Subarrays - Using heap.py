class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for left, right in zip(l, r):
            subArray = nums[left : (right + 1)]
            if len(subArray) == 1:
                result.append(True)
                continue
            heapify(subArray)
            b = heappop(subArray)
            a = heappop(subArray)
            diff = a - b
            tempResult = True
            while subArray:
                b = a
                a = heappop(subArray)
                if a - b != diff:
                    tempResult = False
                    break
            result.append(tempResult)
        return result