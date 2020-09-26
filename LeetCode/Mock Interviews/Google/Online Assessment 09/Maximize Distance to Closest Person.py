class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)
        result = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                result = max(result, min(left, right))
        return result