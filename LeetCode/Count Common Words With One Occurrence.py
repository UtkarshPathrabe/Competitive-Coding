class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        hashMapA, hashMapB = defaultdict(int), defaultdict(int)
        for word in words1:
            hashMapA[word] += 1
        for word in words2:
            if word in hashMapA and hashMapA[word] == 1:
                hashMapB[word] += 1
        result = 0
        for word in hashMapB:
            if hashMapB[word] == 1:
                result += 1
        return result