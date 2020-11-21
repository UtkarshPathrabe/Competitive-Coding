class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0],]
        prev, prevLen = folder[0] + '/', len(folder[0]) + 1
        for f in folder[1:]:
            if f[:prevLen] != prev:
                result.append(f)
                prev, prevLen = f + '/', len(f) + 1
        return result