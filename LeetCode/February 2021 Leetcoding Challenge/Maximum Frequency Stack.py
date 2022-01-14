class FreqStack:

    def __init__(self):
        self.freq, self.freqGroup, self.maxFreq = Counter(), defaultdict(list), 0

    def push(self, x: int) -> None:
        freq = self.freq[x] + 1
        self.freq[x] = freq
        self.freqGroup[freq].append(x)
        if freq > self.maxFreq:
            self.maxFreq = freq

    def pop(self) -> int:
        x = self.freqGroup[self.maxFreq].pop()
        self.freq[x] -= 1
        if not self.freqGroup[self.maxFreq]:
            self.maxFreq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()