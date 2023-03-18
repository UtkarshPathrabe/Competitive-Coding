class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sLen, wordsCount, wordLen, result = len(s), len(words), len(words[0]), []
        substringLen, wordsCountMap = wordLen * wordsCount, Counter(words)
        
        def slidingWindow(left):
            wordsFoundMap, wordsUsed, excessWord = defaultdict(int), 0, False
            # iterate wordLen at a time, and at each iteration we focus on one word
            for right in range(left, sLen, wordLen):
                if right + wordLen > sLen:
                    break
                substring = s[right : right + wordLen]
                # Mismatched word - reset the window
                if substring not in wordsCountMap:
                    wordsFoundMap, wordsUsed, excessWord = defaultdict(int), 0, False
                    left = right + wordLen  # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substringLen or excessWord:
                        # Move the left bound over continously
                        leftmostWord, left = s[left : left + wordLen], left + wordLen
                        wordsFoundMap[leftmostWord] -= 1
                        if wordsFoundMap[leftmostWord] == wordsCountMap[leftmostWord]:
                            # This word was the excess word
                            excessWord = False
                        else:
                            # Otherwise we actually needed it
                            wordsUsed -= 1
                    # Keep track of how many times this word occurs in the window
                    wordsFoundMap[substring] += 1
                    if wordsFoundMap[substring] <= wordsCountMap[substring]:
                        wordsUsed += 1
                    else:
                        # Found too many instances already
                        excessWord = True
                    if wordsUsed == wordsCount and not excessWord:
                        # Found a valid substring
                        result.append(left)
        for i in range(wordLen):
            slidingWindow(i)
        return result