class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        availableSuitTypes, availableRankFreq = len(set(suits)), Counter(ranks)
        if availableSuitTypes == 1:
            return "Flush"
        elif max(availableRankFreq.values()) >= 3:
            return "Three of a Kind"
        elif max(availableRankFreq.values()) == 2:
            return "Pair"
        else:
            return "High Card"