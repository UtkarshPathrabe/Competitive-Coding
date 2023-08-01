class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(startIndex, currentCombination):
            if len(currentCombination) == k:
                result.append(list(currentCombination))
                return
            for i in range(startIndex, n + 1):
                currentCombination.append(i)
                backtrack(i + 1, currentCombination)
                currentCombination.pop()
        backtrack(1, [])
        return result