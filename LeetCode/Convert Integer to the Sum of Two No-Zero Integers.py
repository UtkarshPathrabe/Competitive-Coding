class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n + 1):
            complement = n - i
            if '0' not in set(str(i)) and '0' not in set(str(complement)):
                return [i, complement]