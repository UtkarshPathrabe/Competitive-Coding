class Solution:
    def addBoldTag(self, S: str, words: List[str]) -> str:
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i + len(word), N)):
                        mask[j] = True
        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)