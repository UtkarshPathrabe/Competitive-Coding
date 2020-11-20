class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logsMap = defaultdict(list)
        for log in logs:
            if log.split()[1].isdigit():
                logsMap['digit'].append(log)
            else:
                logsMap['letter'].append((' '.join(log.split()[1:]) + ' ' + log.split()[0], log))
        logsMap['letter'].sort()
        result = list(x[1] for x in logsMap['letter'])
        result.extend(logsMap['digit'])
        return result