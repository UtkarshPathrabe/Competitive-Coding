class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        E = len(trust)
        if E < N - 1:
            return -1
        trustScore = [0] * N
        for a, b in trust:
            trustScore[a - 1] -= 1
            trustScore[b - 1] += 1
        for index, t in enumerate(trustScore, 1):
            if t == N - 1:
                return index
        return -1