class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams, totalMatches = n, 0
        while teams > 1:
            if teams % 2 == 0:
                memo = teams // 2
                totalMatches += memo
                teams = memo
            else:
                memo = (teams - 1) // 2
                totalMatches += memo
                teams = memo + 1
        return totalMatches