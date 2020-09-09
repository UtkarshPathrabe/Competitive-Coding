class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1List, version2List = version1.split('.'), version2.split('.')
        v1Len, v2Len = len(version1List), len(version2List)
        for i in range(max(v1Len, v2Len)):
            num1 = int(version1List[i]) if i < v1Len else 0
            num2 = int(version2List[i]) if i < v2Len else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0