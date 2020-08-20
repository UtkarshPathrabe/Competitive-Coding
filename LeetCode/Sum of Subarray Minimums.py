class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        stack = deque()
        result = dotProduct = 0
        for index, num in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= num:
                oldNum, oldCount = stack.pop()
                count += oldCount
                dotProduct -= oldNum * oldCount
            stack.append((num, count))
            dotProduct += num * count
            result += dotProduct
        return result % MOD