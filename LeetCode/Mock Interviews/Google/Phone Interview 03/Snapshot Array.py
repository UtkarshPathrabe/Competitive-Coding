class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[[0, 0]] for _ in range(length)]
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        _, snapId = self.data[index][-1]
        if snapId == self.snapId:
            self.data[index][-1][0] = val
        else:
            self.data[index].append([val, self.snapId])

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        indexData = self.data[index]
        startIndex, endIndex = 0, len(indexData) - 1
        while startIndex < endIndex:
            mid = startIndex + (endIndex - startIndex) // 2
            val, snapId = indexData[mid]
            if snapId > snap_id:
                endIndex = mid
            else:
                startIndex = mid + 1
        if indexData[startIndex][1] <= snap_id:
            return indexData[startIndex][0]
        return indexData[startIndex - 1][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)