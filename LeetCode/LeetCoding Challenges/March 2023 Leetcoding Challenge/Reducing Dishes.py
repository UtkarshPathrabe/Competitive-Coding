class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @lru_cache(maxsize=None)
        def findMaxSatisfaction(index, time):
            if index == len(satisfaction):
                return 0
            return max(findMaxSatisfaction(index + 1, time), satisfaction[index] * time + findMaxSatisfaction(index + 1, time + 1))
        
        return findMaxSatisfaction(0, 1)