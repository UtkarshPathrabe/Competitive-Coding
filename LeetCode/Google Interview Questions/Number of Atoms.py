class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formulaLength = len(formula)
        i = 0
        stack = deque([defaultdict(int)])
        while i < formulaLength:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                iStart = i
                while i < formulaLength and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[iStart:i] or 1)
                for name, val in top.items():
                    stack[-1][name] += val * multiplicity
            else:
                iStart = i
                i += 1
                while i < formulaLength and formula[i].islower():
                    i += 1
                name = formula[iStart:i]
                iStart = i
                while i < formulaLength and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[iStart:i] or 1)
                stack[-1][name] += multiplicity
        return ''.join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '') for name in sorted(stack[-1]))