class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = deque([num for num in nums][::-1])
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            result[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i])
        return result