class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        p = int((2 * candies + 0.25)**0.5 - 0.5) 
        remaining = int(candies - (p + 1) * p * 0.5)
        rows, cols = p // n, p % n
        d = [0] * n
        for i in range(n):
            d[i] = (i + 1) * rows + int(rows * (rows - 1) * 0.5) * n
            if i < cols:
                d[i] += i + 1 + rows * n
        d[cols] += remaining
        return d