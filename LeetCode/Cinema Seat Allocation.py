class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        graph = defaultdict(set)
        for row, col in reservedSeats:
            graph[row].add(col)
        result = 2 * n
        for row, seats in graph.items():
            familiesAllowed = 0
            if 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats:
                familiesAllowed += 1
            if 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats:
                familiesAllowed += 1
            if 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats and familiesAllowed == 0:
                familiesAllowed += 1
            result += familiesAllowed - 2
        return result