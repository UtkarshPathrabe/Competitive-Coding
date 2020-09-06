class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(abs(x[0] - x[1]) <= a and abs(x[1] - x[2]) <= b and abs(x[0] - x[2]) <= c for x in combinations(arr, 3))