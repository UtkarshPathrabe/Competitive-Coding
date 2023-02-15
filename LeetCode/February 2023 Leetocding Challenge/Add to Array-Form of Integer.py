class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i != 0:
                A[i - 1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A