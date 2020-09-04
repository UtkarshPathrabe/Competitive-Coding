class Solution:
    def longestDupSubstring(self, S: str) -> str:
        base, n, modulus = 26, len(S), 2**32
        nums = [ord(c) - ord('a') for c in S]
        
        def search(L):
            h = 0
            for i in range(L):
                h = ((h * base) + nums[i]) % modulus
            seen = {h}
            baseL = pow(base, L, modulus)
            for i in range(1, n - L + 1):
                h = ((h * base) - (nums[i - 1] * baseL) + nums[i + L - 1]) % modulus
                if h in seen:
                    return i
                seen.add(h)
            return -1
        
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if search(L) == -1:
                right = L - 1
            else:
                left = L + 1
        i = search(left - 1)
        return S[i:i + left - 1]