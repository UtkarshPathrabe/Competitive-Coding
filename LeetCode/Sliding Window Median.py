from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def getMedian(stream):
            midIndex = k // 2
            if k % 2 == 0:
                return (stream[midIndex] + stream[midIndex - 1]) / 2
            else:
                return stream[midIndex]
        stream, n = SortedList(nums[:k]), len(nums)
        result = [getMedian(stream),]
        for i in range(k, n):
            stream.discard(nums[i - k])
            stream.add(nums[i])
            result.append(getMedian(stream))
        return result