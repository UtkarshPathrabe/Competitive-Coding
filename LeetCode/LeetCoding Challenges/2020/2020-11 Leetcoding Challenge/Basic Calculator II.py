# AddSub := MulDiv {[+-] MulDiv}
# MulDiv := Unit {[*/] Unit}
# Unit   := Integer | AddSub
# Integer:= d+

class Solution:
    def calculate(self, s: str) -> int:
        queue = deque(s.replace(' ', '') + '$')
        def addSub():
            result = mulDiv()
            while queue and queue[0] in ('+', '-'):
                sign = queue.popleft()
                if sign == '+':
                    result += mulDiv()
                elif sign == '-':
                    result -= mulDiv()
            return result
        def mulDiv():
            result = unit()
            while queue and queue[0] in ('*', '/'):
                sign = queue.popleft()
                if sign == '*':
                    result *= unit()
                elif sign == '/':
                    result = int(result/unit())
            return result
        def unit():
            if queue[0].isdigit():
                return integer()
            else:
                return addSub()
        def integer():
            result = []
            while queue[0].isdigit():
                result.append(queue.popleft())
            return int(''.join(result))
        return addSub()