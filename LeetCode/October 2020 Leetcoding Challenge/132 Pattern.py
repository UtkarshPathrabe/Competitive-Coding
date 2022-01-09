class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        numberOfItems = len(nums)
        if numberOfItems < 3:
            return False
        stack, minArray = [], [0] * numberOfItems
        minArray[0] = nums[0]
        for i in range(1, numberOfItems):
            minArray[i] = min(minArray[i - 1], nums[i])
        for i in range(numberOfItems - 1, -1, -1):
            if nums[i] > minArray[i]:
                while stack and stack[-1] <= minArray[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False