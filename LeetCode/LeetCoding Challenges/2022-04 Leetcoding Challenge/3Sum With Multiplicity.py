class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD, result = 10**9 + 7, 0
        arr.sort()
        for i, x in enumerate(arr):
            T, j, k = target - x, i + 1, len(arr) - 1
            while j < k:
                if arr[j] + arr[k] < T:
                    j += 1
                elif arr[j] + arr[k] > T:
                    k -= 1
                elif arr[j] != arr[k]:
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        left, j = left + 1, j + 1
                    while k - 1 > j and arr[k] == arr[k - 1]:
                        right, k = right + 1, k - 1
                    result += left * right
                    result %= MOD
                    j, k = j + 1, k - 1
                else:
                    result += (k - j + 1) * (k - j) // 2
                    result %= MOD
                    break
        return result