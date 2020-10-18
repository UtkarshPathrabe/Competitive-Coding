class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        positions = defaultdict(list)
        for i in reversed(range(len(s))):
            positions[int(s[i])].append(i)
        for char in t:
            num = int(char)
            if not positions[num]:
                return False
            i = positions[num][-1]
            for j in range(num):
                if positions[j] and positions[j][-1] < i:
                    return False
            positions[num].pop()
        return True