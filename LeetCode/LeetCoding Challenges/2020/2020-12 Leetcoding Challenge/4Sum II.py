class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count, hashMap = 0, defaultdict(int)
        for a in A:
            for b in B:
                hashMap[a + b] += 1
        for c in C:
            for d in D:
                count += hashMap[-(c + d)]
        return count