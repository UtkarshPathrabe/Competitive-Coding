class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = [False] * len(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= maxCandies:
                result[i] = True
        return result