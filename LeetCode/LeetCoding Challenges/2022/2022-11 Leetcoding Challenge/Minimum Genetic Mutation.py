class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen, bank = { start }, set(bank)
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps
            for c in 'ACGT':
                for i in range(len(node)):
                    neighbour = node[:i] + c + node[i+1:]
                    if neighbour not in seen and neighbour in bank:
                        queue.append((neighbour, steps + 1))
                        seen.add(neighbour)
        return -1