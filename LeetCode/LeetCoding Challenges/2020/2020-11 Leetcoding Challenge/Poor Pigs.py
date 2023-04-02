class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = (minutesToTest // minutesToDie) + 1
        return math.ceil(math.log(buckets) / math.log(states))