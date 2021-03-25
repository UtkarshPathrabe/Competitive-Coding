class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        avg, count, currentSum = total // 3, 0, 0
        for i in arr:
            currentSum += i
            if currentSum == avg:
                count += 1
                currentSum = 0
        return count >= 3