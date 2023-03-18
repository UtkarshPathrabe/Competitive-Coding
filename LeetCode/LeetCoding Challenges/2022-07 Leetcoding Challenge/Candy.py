class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratingsLength = len(ratings)
        if ratingsLength == 0:
            return 0
        candies = [1] * ratingsLength
        for i in range(1, ratingsLength):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        totalCandies = candies[ratingsLength - 1]
        for i in range(ratingsLength - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            totalCandies += candies[i]
        return totalCandies