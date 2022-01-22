class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        currentSum, n, minLength, left = sum(nums), len(nums), float('inf'), 0
        for right in range(n):
            currentSum -= nums[right]
            while currentSum < x and left <= right:
                currentSum += nums[left]
                left += 1
            if currentSum == x:
                minLength = min(minLength, n - 1 - right + left)
        return minLength if minLength != float('inf') else -1