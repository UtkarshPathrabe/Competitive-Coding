class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores, output, index = [], 0, -1
        for op in ops:
            if op == '+':
                newScore = scores[index] + scores[index - 1]
                scores.append(newScore)
                index += 1
                output += newScore
            elif op == 'D':
                newScore = scores[index] * 2
                scores.append(newScore)
                index += 1
                output += newScore
            elif op == 'C':
                record = scores.pop()
                index -= 1
                output -= record
            else:
                scores.append(int(op))
                index += 1
                output += int(op)
        return output