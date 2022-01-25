class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        return sorted(arr, key = lambda x : bin(x)[2:].count('1'))