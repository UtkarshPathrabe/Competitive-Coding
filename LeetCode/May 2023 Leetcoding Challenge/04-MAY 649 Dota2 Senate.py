class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque([])
        rBan, rCount, dBan, dCount = 0, 0, 0, 0
        for index, senator in enumerate(senate):
            if senator == 'R':
                rCount += 1
            else:
                dCount += 1
            queue.append(senator)
        while rCount and dCount:
            senator = queue.popleft()
            if senator == 'R':
                if rBan > 0:
                    rBan -= 1
                    rCount -= 1
                else:
                    dBan += 1
                    queue.append(senator)
            else:
                if dBan > 0:
                    dBan -= 1
                    dCount -= 1
                else:
                    rBan += 1
                    queue.append(senator)
        return 'Radiant' if rCount > 0 else 'Dire'
            