class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jumpMap = {}
        for stone in stones:
            jumpMap[stone] = set()
        jumpMap[stones[0]].add(0)
        for stone in stones:
            for jumpSize in jumpMap[stone]:
                for step in range(jumpSize - 1, jumpSize + 2):
                    if step > 0 and stone + step in jumpMap:
                        jumpMap[stone + step].add(step)
        return len(jumpMap[stones[-1]]) > 0