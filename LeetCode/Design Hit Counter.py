class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
        self.timeWindow = 5 * 60

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        deletionIndex = bisect.bisect(self.hits, timestamp - self.timeWindow)
        if deletionIndex > -1:
            self.hits = self.hits[deletionIndex:]
        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)