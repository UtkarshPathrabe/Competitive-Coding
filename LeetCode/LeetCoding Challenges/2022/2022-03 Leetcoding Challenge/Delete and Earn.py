class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, maxNumber = defaultdict(int), 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            maxNumber = max(maxNumber, num)
        @cache
        def maxPoints(num):
            # Check for base cases
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            # Apply recurrence relation
            return max(maxPoints(num - 1), maxPoints(num - 2) + points[num])
        return maxPoints(maxNumber)