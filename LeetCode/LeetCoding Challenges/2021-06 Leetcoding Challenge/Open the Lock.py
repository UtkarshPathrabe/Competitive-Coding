class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNeighbours(node):
            for i in range(4):
                digit = int(node[i])
                for d in (-1, 1):
                    yield node[:i] + str((digit + d) % 10) + node[i + 1:]
        queue = deque([('0000', 0),])
        visited = {'0000'}
        deadEnds = set(deadends)
        if '0000' in deadEnds:
            return -1
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in deadEnds:
                continue
            for n in getNeighbours(node):
                if n not in visited and n not in deadEnds:
                    visited.add(n)
                    queue.append((n, depth + 1))
        return -1