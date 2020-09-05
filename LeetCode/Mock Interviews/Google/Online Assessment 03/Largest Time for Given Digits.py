class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        maxTime = -1
        for h, i, j, k in permutations(arr):
            hour, minute = h * 10 + i, j * 10 + k
            if hour < 24 and minute < 59:
                maxTime = max(maxTime, hour * 60 + minute)
        return '{:02d}:{:02d}'.format(maxTime // 60, maxTime % 60) if maxTime != -1 else ''