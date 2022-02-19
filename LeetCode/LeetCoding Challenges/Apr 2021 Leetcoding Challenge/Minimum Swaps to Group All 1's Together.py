class Solution:
    def minSwaps(self, data: List[int]) -> int:
        subArraySize, currentOnes, maxOnes, left, right = sum(data), 0, 0, 0, 0
        while right < len(data):
            currentOnes += data[right]
            right += 1
            if right - left > subArraySize:
                currentOnes -= data[left]
                left += 1
            maxOnes = max(maxOnes, currentOnes)
        return subArraySize - maxOnes