class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1Counter, nums2Counter, result = Counter(nums1), Counter(nums2), 0
        
        def isPerfectSquare(n):
            squareRoot = math.sqrt(n)
            return {
                'status': squareRoot - floor(squareRoot) == 0,
                'value': int(floor(squareRoot))
            }
        
        for num2j, num2k in combinations(nums2, 2):
            perfectSquare = isPerfectSquare(num2j * num2k)
            if perfectSquare['status']:
                result += nums1Counter[perfectSquare['value']]
        for num1j, num1k in combinations(nums1, 2):
            perfectSquare = isPerfectSquare(num1j * num1k)
            if perfectSquare['status']:
                result += nums2Counter[perfectSquare['value']]
        return result