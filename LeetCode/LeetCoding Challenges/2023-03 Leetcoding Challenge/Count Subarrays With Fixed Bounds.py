class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # min_position, max_position: the MOST RECENT positions of minK and maxK.
        # left_bound: the MOST RECENT value outside the range [minK, maxK].
        result, minPosition, maxPosition, leftBound = 0, -1, -1, -1
        # Iterate over nums, for each number at index i:
        for i, number in enumerate(nums):
            # If the number is outside the range [minK, maxK], update the most recent left_bound.
            if number < minK or number > maxK:
                leftBound = i
            # If the number is minK or maxK, update the most recent position.
            if number == minK:
                minPosition = i
            if number == maxK:
                maxPosition = i
            # The number of valid subarrays equals the number of elements between left_bound and 
            # the smaller of the two most recent positions.
            result += max(0, min(minPosition, maxPosition) - leftBound)
        return result