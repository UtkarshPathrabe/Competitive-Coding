class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp, longestWordSequenceLength = defaultdict(int), 1
        words.sort(key = lambda x:len(x))
        for word in words:
            presentLength = 1
            # Find all possible predecessors for the current word by removing one letter at a time.
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                presentLength = max(presentLength, dp[predecessor] + 1)
            dp[word] = presentLength
            longestWordSequenceLength = max(longestWordSequenceLength, presentLength)
        return longestWordSequenceLength