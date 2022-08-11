class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freqMap = defaultdict(int)
        def digitSum(num: int):
            result = 0
            while num > 0:
                result += num % 10
                num = num // 10
            return result
        for num in range(lowLimit, highLimit + 1):
            freqMap[digitSum(num)] += 1
        return max(freqMap.values())