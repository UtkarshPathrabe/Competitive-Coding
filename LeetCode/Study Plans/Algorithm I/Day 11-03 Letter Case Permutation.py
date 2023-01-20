class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [[]]
        for char in S:
            n = len(result)
            if char.isalpha():
                for i in range(n):
                    result.append(result[i][:])
                    result[i].append(char.lower())
                    result[n + i].append(char.upper())
            else:
                for i in range(n):
                    result[i].append(char)
        return map("".join, result)