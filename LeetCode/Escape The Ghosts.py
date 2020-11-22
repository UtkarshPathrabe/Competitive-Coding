class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        manhattamDistance = lambda P, Q : (abs(Q[0] - P[0]) + abs(Q[1] - P[1]))
        pacManManhattamDistance = manhattamDistance((0, 0), target)
        return all(pacManManhattamDistance < manhattamDistance(ghost, target) for ghost in ghosts)