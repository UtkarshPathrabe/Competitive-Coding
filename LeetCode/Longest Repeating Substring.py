class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n, base, modulus = len(S), 26, 2**24
        nums = [ord(c) - ord('a') for c in S]
        
        def search(L):
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % modulus
            seen = {h}
            baseL = pow(base, L, modulus)
            for start in range(1, n - L + 1):
                h = ((h * base) - (nums[start - 1] * baseL) + (nums[start + L - 1])) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1
        
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if search(L) != -1:
                left = L + 1
            else:
                right = L - 1
        return left - 1