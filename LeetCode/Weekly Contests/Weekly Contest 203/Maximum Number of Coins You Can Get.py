class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        coins, numberOfPiles = 0, len(piles)
        for i in range(1, numberOfPiles - (numberOfPiles // 3), 2):
            coins += piles[i]
        return coins