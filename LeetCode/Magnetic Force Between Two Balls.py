class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def countBalls(distance: int):
            answer, currentBucket = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - currentBucket >= distance:
                    answer, currentBucket = answer + 1, position[i]
            return answer
    
        low, high, result = 0, position[-1] - position[0], position[-1] - position[0]
        while low <= high:
            mid = low + ((high - low) >> 1)
            # too many balls placed, distance is too small, increase it
            if countBalls(mid) >= m:
                result, low = mid, mid + 1
            # less balls placed, distance is too large, decrease it
            else:
                high = mid - 1
        return result