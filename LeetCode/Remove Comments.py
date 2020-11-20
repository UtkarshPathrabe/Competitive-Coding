class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result, inBlockComment = [], False
        for line in source:
            i = 0
            if not inBlockComment:
                newLine = []
            while i < len(line):
                if line[i : i + 2] == '/*' and not inBlockComment:
                    inBlockComment = True
                    i += 1
                elif line[i : i + 2] == '*/' and inBlockComment:
                    inBlockComment = False
                    i += 1
                elif not inBlockComment and line[i : i + 2] == '//':
                    break
                elif not inBlockComment:
                    newLine.append(line[i])
                i += 1
            if newLine and not inBlockComment:
                result.append(''.join(newLine))
        return result