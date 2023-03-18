class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak, numSet = 0, set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                currentNum, currentStreak = num, 1
                while currentNum + 1 in numSet:
                    currentNum, currentStreak = currentNum + 1, currentStreak + 1
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak