class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        def getNextChunk(version, n, p):
            if p >= n:
                return 0, p
            pEnd = p
            while pEnd < n and version[pEnd] != '.':
                pEnd += 1
            num = int(version[p:pEnd]) if pEnd != n - 1 else int(version[p:n])
            p = pEnd + 1
            return num, p
        
        while p1 < n1 or p2 < n2:
            num1, p1 = getNextChunk(version1, n1, p1)
            num2, p2 = getNextChunk(version2, n2, p2)
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0