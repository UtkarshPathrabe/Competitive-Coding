class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.timeline, votesMap, currentWinner, maximumVotes = [], collections.Counter(), None, 0
        for person, time in zip(persons, times):
            votesMap[person] += 1
            votes = votesMap[person]
            if votes >= maximumVotes:
                if person != currentWinner:
                    currentWinner = person
                    self.timeline.append((time, person))
                maximumVotes = max(votes, maximumVotes)

    def q(self, t: int) -> int:
        index = bisect.bisect(self.timeline, (t, float('inf')), 1)
        return self.timeline[index - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)