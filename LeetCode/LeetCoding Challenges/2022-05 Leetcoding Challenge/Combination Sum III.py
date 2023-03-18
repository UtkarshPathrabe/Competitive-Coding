class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining, combination, start):
            if remaining == 0 and len(combination) == k:
                result.append(list(combination))
                return
            elif remaining < 0 or len(combination) == k:
                return
            for i in range(start, 10):
                combination.append(i)
                backtrack(remaining - i, combination, i + 1)
                combination.pop()
        
        backtrack(n, [], 1)
        return result