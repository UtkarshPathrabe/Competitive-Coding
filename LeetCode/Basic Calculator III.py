# BNF grammar
# as := md {[+-] md}
# md := unit {[*/] unit}
# unit := integer | (as)
# integer := d+

class Solution:
    def calculate(self, s: str) -> int:
        queue = deque(s.replace(' ', '') + '$')
        def addSubtract():
            result = multiplyDivide()
            while queue[0] in ('+', '-'):
                sign = queue.popleft()
                if sign == '+':
                    result = result + multiplyDivide()
                else:
                    result = result - multiplyDivide()
            return result
        def multiplyDivide():
            result = unit()
            while queue[0] in ('*', '/'):
                sign = queue.popleft()
                if sign == '*':
                    result = result * unit()
                else:
                    result = int(result / unit())
            return result
        def unit():
            if queue[0].isdigit():
                return integer()
            queue.popleft()
            result = addSubtract()
            queue.popleft()
            return result
        def integer():
            result = []
            while queue[0].isdigit():
                result.append(queue.popleft())
            return int(''.join(result))
        return addSubtract()