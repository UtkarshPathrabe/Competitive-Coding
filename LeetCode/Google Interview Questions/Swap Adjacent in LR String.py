class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if start.count('X') != end.count('X'):
            return False
        if start.replace('X', '') != end.replace('X', ''):
            return False
        i, j, n = 0, 0, len(start)
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i == n or j == n:
                return i == n and j == n
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True