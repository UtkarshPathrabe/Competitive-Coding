class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low, high, result = 0, len(S), []
        for char in S:
            if char == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        return result + [low]