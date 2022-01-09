class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        maxTime = -1
        for h, i, j, k in permutations(A):
            hour = h * 10 + i
            minute = j * 10 + k
            if hour < 24 and minute < 60:
                maxTime = max(maxTime, hour * 60 + minute)
        if maxTime == -1:
            return ''
        else:
            return '{:02d}:{:02d}'.format(maxTime // 60, maxTime % 60)