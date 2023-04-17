# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        @lru_cache(maxsize = None)
        def knowsCache(a, b):
            return knows(a, b)
        
        def isCelebrity(i):
            for j in range(n):
                if i == j:
                    continue
                if knowsCache(i, j) or not knowsCache(j, i):
                    return False
            return True
        
        celebrityCandidate = 0
        for i in range(1, n):
            if knowsCache(celebrityCandidate, i):
                celebrityCandidate = i
        if isCelebrity(celebrityCandidate):
            return celebrityCandidate
        return -1