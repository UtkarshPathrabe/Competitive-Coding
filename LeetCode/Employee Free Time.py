"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events, OPEN, CLOSE = [], 0, 1
        for employee in schedule:
            for interval in employee:
                events.append((interval.start, OPEN))
                events.append((interval.end, CLOSE))
        events.sort()
        result, prev, balance = [], None, 0
        for time, state in events:
            if balance == 0 and prev is not None:
                result.append(Interval(prev, time))
            prev = time
            balance += 1 if state is OPEN else -1
        return result