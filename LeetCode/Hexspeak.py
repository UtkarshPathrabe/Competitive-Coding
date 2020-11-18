class Solution:
    def toHexspeak(self, num: str) -> str:
        hexList = list(hex(int(num))[2:].upper())
        validChars = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}
        result = []
        for char in hexList:
            if char.isdigit():
                if char not in ['0', '1']:
                    return 'ERROR'
                else:
                    result.append('I' if char == '1' else 'O')
            if char in validChars:
                result.append(char)
        return ''.join(result)