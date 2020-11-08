class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        result = [1] + [0] * len(target)
        for i in range(len(words[0])):
            counter = Counter(w[i] for w in words)
            for j in range(min(i + 1, len(target)), 0, -1):
                result[j] = (result[j] + (result[j - 1] * counter[target[j - 1]])) % 1000000007
        return result[len(target)]