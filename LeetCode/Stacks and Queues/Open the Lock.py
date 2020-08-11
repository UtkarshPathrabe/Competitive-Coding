class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNeighbours(node):
            for i in range(4):
                currentDigit = int(node[i])
                for d in (-1, 1):
                    newDigit = (currentDigit + d) % 10
                    yield node[:i] + str(newDigit) + node[i+1:]
        
        deadNodes = set(deadends)
        queue = deque([('0000', 0)])
        seenNodes = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in deadNodes:
                continue
            for neighbour in getNeighbours(node):
                if neighbour not in seenNodes:
                    seenNodes.add(neighbour)
                    queue.append((neighbour, depth + 1))
        return -1