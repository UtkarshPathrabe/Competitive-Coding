class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingNumbersLength, lastMissedNumber = 0, 0
        number, i = 1, 0
        while missingNumbersLength < k:
            if i < len(arr) and number == arr[i]:
                number += 1
                i += 1
            else:
                lastMissedNumber = number
                missingNumbersLength += 1
                number += 1
        return lastMissedNumber