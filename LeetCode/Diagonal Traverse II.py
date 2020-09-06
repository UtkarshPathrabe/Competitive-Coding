class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        elements = []
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                elements.append((row + col, row * -1, nums[row][col]))
        elements.sort()
        return [x[2] for x in elements]