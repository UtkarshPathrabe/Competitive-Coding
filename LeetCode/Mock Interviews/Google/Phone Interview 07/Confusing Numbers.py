class Solution:
    def confusingNumber(self, N: int) -> bool:
        SAME_UP_DOWN = ['0', '1', '8']
        SAME_LEFT_RIGHT = ['6', '9']
        s = str(N)
        numLength = len(s)
        if numLength == 1:
            return s in SAME_LEFT_RIGHT
        temp = []
        for ch in s:
            if ch in SAME_UP_DOWN:
                temp.append(ch)
            elif ch == '6':
                temp.append('9')
            elif ch == '9':
                temp.append('6')
            else:
                return False
        return ''.join(temp)[::-1] != s