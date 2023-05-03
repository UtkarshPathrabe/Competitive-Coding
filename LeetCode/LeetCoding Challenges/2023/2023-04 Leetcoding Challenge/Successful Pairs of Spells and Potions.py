class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        n = len(potions)
        maxPotion = potions[n - 1]
        for spell in spells:
            minPotion = (success + spell - 1) // spell
            if minPotion > maxPotion:
                result.append(0)
                continue
            index = bisect.bisect_left(potions, minPotion)
            result.append(n - index)
        return result