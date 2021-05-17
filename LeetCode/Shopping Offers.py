class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        hashMap = {}
        def dotProduct(a, b):
            currentSum = 0
            for x, y in zip(a, b):
                currentSum += x * y
            return currentSum
        def shopping(needs):
            if sum(needs) == 0:
                return 0
            if tuple(needs) in hashMap:
                return hashMap[tuple(needs)]
            result = dotProduct(needs, price)
            for s in special:
                needsClone = list(needs)
                j = 0
                while j < len(needs):
                    diff = needsClone[j] - s[j]
                    if diff < 0:
                        break
                    needsClone[j] = diff
                    j += 1
                if j == len(needs):
                    result = min(result, s[j] + shopping(needsClone))
            hashMap[tuple(needs)] = result
            return result
        return shopping(needs)