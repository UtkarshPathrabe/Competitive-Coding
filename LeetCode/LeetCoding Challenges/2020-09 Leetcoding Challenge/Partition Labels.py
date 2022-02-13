class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndexOf = {c: i for i, c in enumerate(S)}
        anchor = j = 0
        result = []
        for i, c in enumerate(S):
            j = max(j, lastIndexOf[c])
            if i == j:
                result.append(i - anchor + 1)
                anchor = i + 1
        return result