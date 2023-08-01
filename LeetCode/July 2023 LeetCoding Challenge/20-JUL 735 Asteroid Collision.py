class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            while result and asteroid < 0 < result[-1]:
                if result[-1] < -asteroid:
                    result.pop()
                    continue
                elif result[-1] == -asteroid:
                    result.pop()
                break
            else:
                result.append(asteroid)
        return result