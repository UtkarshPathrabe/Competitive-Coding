class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        counts = [count for number, count in counts.most_common()]
        setSize, totalRemoved = 0, 0
        for count in counts:
            totalRemoved, setSize = totalRemoved + count, setSize + 1
            if totalRemoved >= (len(arr) // 2):
                break
        return setSize