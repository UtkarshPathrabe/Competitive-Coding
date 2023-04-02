class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sLen, result = len(s), []
        dp = [[False] * sLen for _ in range(sLen)]
        def backtrack(start, currentList):
            nonlocal dp, result, s
            if start >= sLen:
                result.append(list(currentList))
            else:
                for end in range(start, sLen):
                    if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                        dp[start][end] = True
                        currentList.append(s[start:end + 1])
                        backtrack(end + 1, currentList)
                        currentList.pop()
        backtrack(0, [])
        return result