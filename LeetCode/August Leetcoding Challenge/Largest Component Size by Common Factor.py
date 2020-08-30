class DisjointSetUnion:
    
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return px
        if self.size[px] > self.size[py]:
            px, py = py, px
        self.parent[px] = py
        self.size[py] += self.size[px]
        return py

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def getDistinctPrimeFactors(num):
            factor, primeFactors = 2, set()
            while num >= factor * factor:
                if num % factor:
                    factor += 1
                else:
                    primeFactors.add(factor)
                    num //= factor
            primeFactors.add(num)
            return primeFactors
        dsu = DisjointSetUnion(max(A))
        factorMap = dict()
        for num in A:
            primeFactors = list(getDistinctPrimeFactors(num))
            factorMap[num] = primeFactors[0]
            for i in range(len(primeFactors) - 1):
                dsu.union(primeFactors[i], primeFactors[i + 1])
        maxSize, groupCount = 0, defaultdict(int)
        for num in A:
            groupId = dsu.find(factorMap[num])
            groupCount[groupId] += 1
            maxSize = max(maxSize, groupCount[groupId])
        return maxSize