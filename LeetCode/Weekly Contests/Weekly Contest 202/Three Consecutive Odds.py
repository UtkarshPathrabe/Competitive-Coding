class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        numberOfOdds = 0
        for num in arr:
            if num % 2:
                numberOfOdds += 1
            else:
                numberOfOdds = 0
            if numberOfOdds >= 3:
                return True
        return False