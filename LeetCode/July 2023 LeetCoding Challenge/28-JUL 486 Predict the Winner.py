class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def maximumDifference(leftIndex: int, rightIndex: int) -> int:
            if leftIndex == rightIndex:
                return nums[leftIndex]
            scoreByLeft = nums[leftIndex] - maximumDifference(leftIndex + 1, rightIndex)
            scoreByRight = nums[rightIndex] - maximumDifference(leftIndex, rightIndex - 1)
            return max(scoreByLeft, scoreByRight)
        return maximumDifference(0, len(nums) - 1) >= 0