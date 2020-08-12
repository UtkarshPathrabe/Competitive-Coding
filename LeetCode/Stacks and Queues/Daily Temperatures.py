class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        inputArrayLength = len(T)
        result = [0] * inputArrayLength
        stack = deque()
        for i in range(inputArrayLength - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result