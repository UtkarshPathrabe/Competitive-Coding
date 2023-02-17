class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        freqMap = defaultdict(int)
        for match in matches:
            freqMap[match[0]] += 0
            freqMap[match[1]] += 1
        noMatchesLost, oneMatchLost = set(), set()
        for player, lostCount in freqMap.items():
            if lostCount == 0:
                noMatchesLost.add(player)
            elif lostCount == 1:
                oneMatchLost.add(player)
        return [sorted(noMatchesLost), sorted(oneMatchLost)]