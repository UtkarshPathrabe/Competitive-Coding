class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visitedIndices, queue = set([start,]), deque([start,])
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            for neighbour in (index + arr[index], index - arr[index]):
                if 0 <= neighbour < len(arr) and neighbour not in visitedIndices:
                    queue.append(neighbour)
                    visitedIndices.add(neighbour)
        return False