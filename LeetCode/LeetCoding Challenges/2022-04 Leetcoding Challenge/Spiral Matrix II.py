class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result, count = [[0] * n for _ in range(n)], 1
        for layer in range((n + 1) // 2):
            for col in range(layer, n - layer):
                result[layer][col] = count
                count += 1
            for row in range(layer + 1, n - layer):
                result[row][n - layer - 1] = count
                count += 1
            for col in range(n - layer - 2, layer - 1, -1):
                result[n - layer - 1][col] = count
                count += 1
            for row in range(n - layer - 2, layer, -1):
                result[row][layer] = count
                count += 1
        return result