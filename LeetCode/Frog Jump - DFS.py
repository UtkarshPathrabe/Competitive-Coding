class Solution:
    def canCross(self, stones: List[int]) -> bool:
        for i in range(1, len(stones)):
            if stones[i] > i + stones[i - 1]:
                return False
        stack = deque([(stones[0], 0)])
        availableStonePositions = set(stones)
        while stack:
            position, jumpSize = stack.pop()
            for step in range(jumpSize - 1, jumpSize + 2):
                if step <= 0:
                    continue
                if position + step == stones[-1]:
                    return True
                if position + step in availableStonePositions:
                    stack.append((position + step, step))
        return False