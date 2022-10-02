class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileContentMap, result = defaultdict(list), []
        for path in paths:
            pathContents = path.split()
            for i in range(1, len(pathContents)):
                fileName, content = pathContents[i].split('(')
                content = content.split(')')[0]
                fileContentMap[content].append(pathContents[0] + '/' + fileName)
        for content, files in fileContentMap.items():
            if len(files) > 1:
                result.append(files)
        return result