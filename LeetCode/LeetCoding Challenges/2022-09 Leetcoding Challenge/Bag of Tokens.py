class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        tokens, maxScore, currentScore = deque(tokens), 0, 0
        while tokens and (P >= tokens[0] or currentScore):
            while tokens and P >= tokens[0]:
                P -= tokens.popleft()
                currentScore += 1
            maxScore = max(maxScore, currentScore)
            if tokens and currentScore:
                P += tokens.pop()
                currentScore -= 1
        return maxScore