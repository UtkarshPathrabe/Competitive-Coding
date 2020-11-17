class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap, maxGroupSize = defaultdict(int), 0
        def getDigitSum(x):
            currentSum = 0
            while x:
                currentSum += (x % 10)
                x //= 10
            return currentSum
        for i in range(1, n + 1):
            hashMap[getDigitSum(i)] += 1
            maxGroupSize = max(maxGroupSize, hashMap[getDigitSum(i)])
        return sum(1 for _, val in hashMap.items() if val == maxGroupSize)