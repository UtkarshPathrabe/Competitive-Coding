class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n, count = len(arr), 0
        for i in range(n - m):
            if arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0
            if count == (m * (k - 1)):
                return True
        return False