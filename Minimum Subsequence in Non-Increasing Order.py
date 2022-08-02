class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums, reverse=True)
        total, result, currentSum = sum(sortedNums), [], 0
        for num in sortedNums:
            if currentSum + num > total - num:
                result.append(num)
                return result
            else:
                currentSum += num
                result.append(num)
                total -= num