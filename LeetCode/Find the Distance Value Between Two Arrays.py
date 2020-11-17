class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        result = 0
        for num in arr1:
            index = bisect.bisect_left(arr2, num)
            if index == 0:
                if abs(num - arr2[index]) > d:
                    result += 1
            elif index == len(arr2):
                if abs(num - arr2[index - 1]) > d:
                    result += 1
            else:
                if abs(num - arr2[index - 1]) > d and abs(num - arr2[index]) > d:
                    result += 1
        return result