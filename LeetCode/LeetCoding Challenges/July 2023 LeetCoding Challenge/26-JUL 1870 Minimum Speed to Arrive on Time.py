class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def timeRequired(speed):
            time = 0.0
            for index, d in enumerate(dist):
                t = d / speed
                time += t if (index == (len(dist) - 1)) else math.ceil(t)
            return time
        
        left, right, minSpeed = 1, 10000000, -1
        while left <= right:
            mid = (left + right) >> 1
            if timeRequired(mid) <= hour:
                # Move to the left half.
                minSpeed = mid
                right = mid - 1
            else:
                # Move to the right half.
                left = mid + 1
        return minSpeed