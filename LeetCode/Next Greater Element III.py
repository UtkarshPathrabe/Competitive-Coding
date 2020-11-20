class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        i, j = len(num) - 2, len(num) - 1
        while i > -1 and num[i] >= num[i + 1]:
            i -= 1
        if i < 0:
            return -1
        while j >= 0 and num[j] <= num[i]:
            j -= 1
        num[i], num[j] = num[j], num[i]
        low, high = i + 1, len(num) - 1
        while low < high:
            num[low], num[high] = num[high], num[low]
            low += 1
            high -= 1
        try:
            result = int(''.join(num))
            return result if result < 2 ** 31 else -1
        except:
            return -1