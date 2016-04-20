class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        length, i, j = len(self.__elements), 0, 0
        while i < length:
            j = i + 1
            while j < length:
                self.maximumDifference = max(self.maximumDifference, abs(self.__elements[i]-self.__elements[j]))
                j += 1
            i += 1

# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference