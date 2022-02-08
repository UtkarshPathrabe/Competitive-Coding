class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transform = ''.join([str(ord(c) - ord('a') + 1) for c in s])
        for itr in range(k):
            transform = str(sum([int(i) for i in transform]))
        return int(transform)