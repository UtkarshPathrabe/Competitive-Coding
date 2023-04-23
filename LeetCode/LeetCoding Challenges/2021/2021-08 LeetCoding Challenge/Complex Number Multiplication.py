class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        aReal, aImg, bReal, bImg = int(a.split('+')[0]), int(a.split('+')[1][:-1]), int(b.split('+')[0]), int(b.split('+')[1][:-1])
        return str((aReal * bReal) - (aImg * bImg)) + '+' + str((aReal * bImg) + (bReal * aImg)) + 'i'