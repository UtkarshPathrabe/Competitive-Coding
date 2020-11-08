class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        sLength, tLength, result = len(s), len(t), 0
        sameDP = [[0 for _ in range(tLength + 1)] for _ in range(sLength + 1)]
        diffDP = [[0 for _ in range(tLength + 1)] for _ in range(sLength + 1)]
        for i in range(sLength):
            for j in range(tLength):
                sameDP[i + 1][j + 1] = (sameDP[i][j] + 1) if s[i] == t[j] else 0
        for i in range(sLength):
            for j in range(tLength):
                diffDP[i + 1][j + 1] = diffDP[i][j] if s[i] == t[j] else sameDP[i][j] + 1
        for i in range(sLength + 1):
            result += sum(diffDP[i])
        return result