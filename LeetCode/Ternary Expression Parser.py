# unit := d | [TF] | ternary
# ternary := [TF] ? unit : unit

class Solution:
    def parseTernary(self, expression: str) -> str:
        queue = deque(expression + '$')
        def unit():
            return queue.popleft() if queue[1] != '?' else ternary()
        def ternary():
            condition = queue.popleft()
            queue.popleft()
            left = unit()
            queue.popleft()
            right = unit()
            if condition == 'T':
                return left
            else:
                return right
        return unit()