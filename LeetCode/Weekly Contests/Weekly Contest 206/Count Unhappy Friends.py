class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ranks, partners, unhappy = {}, defaultdict(int), 0
        for p1, pref in enumerate(preferences):
            ranks[p1] = defaultdict(lambda : n)
            for rank, p2 in enumerate(pref):
                ranks[p1][p2] = rank
        for p1, p2 in pairs:
            partners[p1] = p2
            partners[p2] = p1
        for p1, p2 in pairs:
            for peer in preferences[p1]:
                if ranks[p1][peer] < ranks[p1][p2] and ranks[peer][p1] < ranks[peer][partners[peer]]:
                    unhappy += 1
                    break
            for peer in preferences[p2]:
                if ranks[p2][peer] < ranks[p2][p1] and ranks[peer][p2] < ranks[peer][partners[peer]]:
                    unhappy += 1
                    break
        return unhappy