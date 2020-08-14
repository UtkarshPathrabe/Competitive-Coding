class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        numLength = len(num)
        sameUpDown = ['0', '1', '8']
        sameLeftRight = ['6', '9']
        if numLength == 0:
            return True
        elif numLength == 1:
            return num in sameUpDown
        else:
            temp = ''
            for i, n in enumerate(num):
                if n in sameUpDown + sameLeftRight:
                    if n == sameLeftRight[0]:
                        temp += sameLeftRight[1]
                    elif n == sameLeftRight[1]:
                        temp += sameLeftRight[0]
                    else:
                        temp += n
                else:
                    return False
            return temp[::-1] == num