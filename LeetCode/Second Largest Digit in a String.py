class Solution:
    def secondHighest(self, s: str) -> int:
        sortedDigits = sorted(set([int(i) for i in s if i.isdigit()]))
        return sortedDigits[-2] if len(sortedDigits) > 1 else -1