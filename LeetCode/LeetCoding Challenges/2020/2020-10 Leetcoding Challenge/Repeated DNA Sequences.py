class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []
        base = 4
        baseL = pow(base, L)
        charMap = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [charMap[char] for char in s]
        currentHash = 0
        for num in nums[:L]:
            currentHash = (currentHash * base) + num
        seen, result = set([currentHash,]), set()
        for i in range(1, n - L + 1):
            currentHash = ((currentHash * base) - (nums[i - 1] * baseL)) + nums[i + L - 1]
            if currentHash in seen:
                result.add(s[i : i + L])
            seen.add(currentHash)
        return result