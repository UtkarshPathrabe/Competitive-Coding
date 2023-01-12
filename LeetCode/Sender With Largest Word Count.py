class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        freqMap = defaultdict(int)
        for i in range(len(senders)):
            freqMap[senders[i]] += len(messages[i].split(' '))
        maxCount, sender = 0, ''
        for s, freq in freqMap.items():
            if freq > maxCount:
                maxCount, sender = freq, s
            elif freq == maxCount and sender < s:
                sender = s
        return sender