class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, resultMap, result = deque(), defaultdict(int), []
        for num in nums2:
            while stack and stack[-1] < num:
                resultMap[stack.pop()] = num
            stack.append(num)
        while stack:
            resultMap[stack.pop()] = -1
        for num in nums1:
            result.append(resultMap[num])
        return result