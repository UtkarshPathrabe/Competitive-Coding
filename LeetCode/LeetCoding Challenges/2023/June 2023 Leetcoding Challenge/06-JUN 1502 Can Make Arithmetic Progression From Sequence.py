class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortedArr = sorted(arr)
        diff = sortedArr[1] - sortedArr[0]
        for i in range(2, len(sortedArr)):
            if (sortedArr[i] - sortedArr[i - 1]) != diff:
                return False
        return True