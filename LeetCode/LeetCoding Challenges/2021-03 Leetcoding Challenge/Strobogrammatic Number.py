class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        numLength = len(num)
        SAME_UP_DOWN = ['0', '1', '8']
        SAME_LATERAL = ['6', '9']
        if numLength == 0:
            return True
        elif numLength == 1:
            return num in SAME_UP_DOWN
        else:
            tempNum = []
            for ch in num:
                if ch in SAME_UP_DOWN:
                    tempNum.append(ch)
                elif ch == '6':
                    tempNum.append('9')
                elif ch == '9':
                    tempNum.append('6')
                else:
                    return False
            return ''.join(tempNum)[::-1] == num