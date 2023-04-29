class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total, N, sides = sum(matchsticks), len(matchsticks), [0] * 4
        side = total // 4
        matchsticks.sort(reverse = True)
        if total % 4 != 0 or N < 4 or matchsticks[0] > side:
            return False
        def alreadyConsidered(sides, position):
            for i in range(position):
                if sides[i] == sides[position]:
                    return True
            return False
        def backtrack(sides, position):
            if position == N:
                return side == sides[0] == sides[1] == sides[2] == sides[3]
            for i in range(4):
                if sides[i] + matchsticks[position] > side or alreadyConsidered(sides, i):
                    continue
                sides[i] += matchsticks[position]
                if backtrack(sides, position + 1):
                    return True
                sides[i] -= matchsticks[position]
            return False
        return backtrack(sides, 0)