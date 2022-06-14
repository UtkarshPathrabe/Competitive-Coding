class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i - k : i] for i in range(k, len(s) + 1)}) == 1 << k