class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([list(s) != sorted(s) for s in zip(*strs)])