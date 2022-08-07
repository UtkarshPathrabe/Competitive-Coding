class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        for index, t in enumerate(tickets):
            if index <= k:
                total += min(t, tickets[k])
            else:
                total += min(t, tickets[k] - 1)
        return total