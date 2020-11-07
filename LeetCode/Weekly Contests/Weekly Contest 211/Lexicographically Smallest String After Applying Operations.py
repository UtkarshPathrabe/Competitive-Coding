class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        result, queue, visited = s, deque([s,]), {s}
        while queue:
            currentString = queue.popleft()
            if currentString < result:
                result = currentString
            addAList = list(currentString)
            for i, c in enumerate(addAList):
                if i % 2:
                    addAList[i] = str((int(c) + a) % 10)
            addA = ''.join(addAList)
            if addA not in visited:
                visited.add(addA)
                queue.append(addA)
            rotateB = currentString[-b:] + currentString[:-b]
            if rotateB not in visited:
                visited.add(rotateB)
                queue.append(rotateB)
        return result