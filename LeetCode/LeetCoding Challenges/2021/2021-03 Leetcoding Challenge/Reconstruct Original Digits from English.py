class Solution:
    def originalDigits(self, s: str) -> str:
        freqMap, result = Counter(s), defaultdict(int)
        # letter 'z' is present only in 'zero'
        result['0'] = freqMap['z']
        # letter 'w' is present only in 'two'
        result['2'] = freqMap['w']
        # letter 'u' is present only in 'four'
        result['4'] = freqMap['u']
        # letter 'x' is present only in 'six'
        result['6'] = freqMap['x']
        # letter 'g' is present only in 'eight'
        result['8'] = freqMap['g']
        # letter 'h' is present only in 'three' and 'eight'
        result['3'] = freqMap['h'] - result['8']
        # letter 'f' is present only in 'four' and 'five'
        result['5'] = freqMap['f'] - result['4']
        # letter 's' is present only in 'six' and 'seven'
        result['7'] = freqMap['s'] - result['6']
        # letter 'i' is present in 'five', 'six', 'eight' and 'nine'
        result['9'] = freqMap['i'] - result['5'] - result['6'] - result['8']
        # letter 'n' is present in 'one', 'seven' and 'nine'
        result['1'] = freqMap['n'] - result['7'] - (2 * result['9'])
        return ''.join([key * result[key] for key in sorted(result.keys())])