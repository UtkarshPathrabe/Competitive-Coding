class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counter = Counter(A)
        for num, freq in sorted(counter.items(), reverse = True):
            if freq == 1:
                return num
        return -1