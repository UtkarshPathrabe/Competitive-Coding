class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possibleDups, arrLength = 0, len(arr) - 1
        for i in range(arrLength + 1):
            if i > arrLength - possibleDups:
                break
            if arr[i] == 0:
                if i == arrLength - possibleDups:
                    arr[arrLength] = 0
                    arrLength -= 1
                    break
                possibleDups += 1
        last = arrLength - possibleDups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possibleDups] = 0
                possibleDups -= 1
                arr[i + possibleDups] = 0
            else:
                arr[i + possibleDups] = arr[i]