class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag):
            N = len(frag)
            for d in range(1, N + 1):
                left, right = frag[:d], frag[d:]
                if ((not left.startswith('0') or left == '0') and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right
        S = s[1: -1]
        return ["({}, {})".format(*cand) for i in range(1, len(S)) for cand in itertools.product(make(S[:i]), make(S[i:]))]