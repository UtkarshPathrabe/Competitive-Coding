class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, heightsLength, maxArea = deque([-1,]), len(heights), 0
        for i, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= height:
                currentHeight, currentWidth = heights[stack.pop()], i - stack[-1] - 1
                maxArea = max(maxArea, currentHeight * currentWidth)
            stack.append(i)
        while stack[-1] != -1:
            currentHeight, currentWidth = heights[stack.pop()], heightsLength - stack[-1] - 1
            maxArea = max(maxArea, currentHeight * currentWidth)
        return maxArea