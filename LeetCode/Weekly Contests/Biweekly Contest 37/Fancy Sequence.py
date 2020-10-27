class Fancy:

    def __init__(self):
        self.mul, self.inc, self.mod, self.size, self.seq = 1, 0, 10**9 + 7, 0, []

    def append(self, val: int) -> None:
        self.seq.append((val, self.mul, self.inc))
        self.size += 1

    def addAll(self, inc: int) -> None:
        self.inc += inc

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.inc = (self.inc * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= self.size:
            return  -1
        val, mul, inc = self.seq[idx]
        ratio = self.mul * pow(mul, self.mod - 2, self.mod)
        return ((val * ratio) + self.inc - (inc * ratio)) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)