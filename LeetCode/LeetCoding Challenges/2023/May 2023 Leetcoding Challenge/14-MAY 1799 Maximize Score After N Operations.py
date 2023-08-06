class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def backtrack(mask: int, pairsPicked: int) -> int:
            # If we have picked all the numbers from 'nums' array, we can't get more score.
            if 2 * pairsPicked == len(nums):
                return 0
            maxScore = 0
            # Iterate on 'nums' array to pick the first and second number of the pair.
            for firstIndex in range(len(nums)):
                for secondIndex in range(firstIndex + 1, len(nums)):
                    # If the numbers are same, or already picked, then we move to next number.
                    if (mask >> firstIndex) & 1 == 1 or (mask >> secondIndex) & 1 == 1:
                        continue
                    # Both numbers are marked as picked in this new mask.
                    newMask = mask | (1 << firstIndex) | (1 << secondIndex)
                    # Calculate score of current pair of numbers, and the remaining array.
                    currScore = (pairsPicked + 1) * math.gcd(nums[firstIndex], nums[secondIndex])
                    remainingScore = backtrack(newMask, pairsPicked + 1)
                    # Store the maximum score.
                    maxScore = max(maxScore, currScore + remainingScore)
                    # We will use old mask in loop's next interation,
                    # means we discarded the picked number and backtracked.
            return maxScore
        return backtrack(0, 0)