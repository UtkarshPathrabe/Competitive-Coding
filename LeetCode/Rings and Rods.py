class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        hashMap = [[False, False, False] for _ in range(10)]
        charMap = {'R': 0, 'G': 1, 'B': 2}
        for i in range(0, len(rings), 2):
            hashMap[int(rings[i + 1])][charMap[rings[i]]] = True
        count = 0
        for m in hashMap:
            if m[0] == m[1] == m[2] == True:
                count += 1
        return count