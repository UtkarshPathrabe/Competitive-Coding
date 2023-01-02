class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        countArray = [0] * (n + 1)
        for citation in citations:
            countArray[min(citation, n)] += 1
        k = n
        s = countArray[k]
        while k > s:
            k -= 1
            s += countArray[k]
        return k