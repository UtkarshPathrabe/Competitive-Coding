class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxTillNow = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maxTillNow = maxTillNow, max(arr[i], maxTillNow)
        return arr