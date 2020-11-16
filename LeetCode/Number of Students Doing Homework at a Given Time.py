class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                result += 1
        return result