class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        numbers = list(count.keys())
        
        def partition(left, right, pivotIndex):
            pivotFrequency = count[numbers[pivotIndex]]
            numbers[pivotIndex], numbers[right] = numbers[right], numbers[pivotIndex]
            index = left
            for i in range(left, right):
                if count[numbers[i]] < pivotFrequency:
                    numbers[index], numbers[i] = numbers[i], numbers[index]
                    index += 1
            numbers[index], numbers[right] = numbers[right], numbers[index]
            return index
        
        def quickSelect(left, right, kSmallest):
            if left == right:
                return
            pivotIndex = partition(left, right, random.randint(left, right))
            if kSmallest == pivotIndex:
                return
            elif kSmallest < pivotIndex:
                quickSelect(left, pivotIndex - 1, kSmallest)
            else:
                quickSelect(pivotIndex + 1, right, kSmallest)
        
        numbersLen = len(numbers)
        quickSelect(0, numbersLen - 1, numbersLen - k)
        return numbers[numbersLen - k:]