class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        parent, size, result, bitsArray, count = [x for x in range(n)], [1] * n, -1, [0] * n, Counter()
        
        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
        
        def union(x, y):
            xParent, yParent = find(x), find(y)
            if xParent == yParent:
                return
            if size[xParent] < size[yParent]:
                xParent, yParent = yParent, xParent
            parent[yParent] = xParent
            size[xParent] += size[yParent]
            size[yParent] = size[xParent]
        
        def getSize(x):
            return size[find(x)]
        
        for step, index in enumerate(arr, start = 1):
            index -= 1
            bitsArray[index], currentSize = 1, 1
            if index - 1 >= 0 and bitsArray[index - 1] == 1:
                leftSize = getSize(index - 1)
                union(index, index - 1)
                currentSize += leftSize
                count[leftSize] -= 1
            if index + 1 < n and bitsArray[index + 1] == 1:
                rightSize = getSize(index + 1)
                union(index, index + 1)
                currentSize += rightSize
                count[rightSize] -= 1
            count[currentSize] += 1
            if count[m] > 0:
                result = step
        return result