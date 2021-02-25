class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i - 1] == '(':
                    result += 1 << bal
        return result