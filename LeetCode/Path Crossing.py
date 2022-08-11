class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited, current = set([(0, 0)]), [0, 0]
        for p in path:
            if p == 'N':
                current[1] += 1
            elif p == 'S':
                current[1] -= 1
            elif p == 'E':
                current[0] += 1
            else:
                current[0] -= 1
            newPoint = (current[0], current[1])
            if newPoint not in visited:
                visited.add(newPoint)
            else:
                return True
        return False