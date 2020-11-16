class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB, setB = sum(A), sum(B), set(B)
        for x in A:
            if x + ((sumB - sumA) // 2) in setB:
                return [x, x + ((sumB - sumA) // 2)]