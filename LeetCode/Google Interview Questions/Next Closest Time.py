class Solution:
    def nextClosestTime(self, time: str) -> str:
        result = start = int(time[:2]) * 60 + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            hours, minutes = h1 * 10 + h2, m1 * 10 + m2
            if hours < 24 and minutes < 60:
                current = hours * 60 + minutes
                timeElapsed = (current - start) % (24 * 60)
                if 0 < timeElapsed < elapsed:
                    result = current
                    elapsed = timeElapsed
        answer = divmod(result, 60)
        return '{:02d}:{:02d}'.format(answer[0], answer[1])