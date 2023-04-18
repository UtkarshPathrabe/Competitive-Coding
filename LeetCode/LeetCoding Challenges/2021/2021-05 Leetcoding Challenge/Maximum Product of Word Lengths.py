class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n, maxVal = len(words), 0
        masks, lens = [0] * n, [0] * n
        bitNumber = lambda ch: ord(ch) - ord('a')
        for i in range(n):
            bitMask = 0
            for ch in words[i]:
                # add bit number bitNumber in bitMask
                bitMask |= 1 << bitNumber(ch)
            masks[i] = bitMask
            lens[i] = len(words[i])
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    maxVal = max(maxVal, lens[i] * lens[j])
        return maxVal