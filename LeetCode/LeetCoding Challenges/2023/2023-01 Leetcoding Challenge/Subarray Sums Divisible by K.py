class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod, result = 0, 0
        modGroups = defaultdict(int)
        modGroups[0] = 1
        for num in nums:
            # Take modulo twice to avoid negative remainders.
            prefixMod = (prefixMod + (num % k) + k) % k
            # Add the count of subarrays that have the same remainder as the current
            # one to cancel out the remainders.
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1
        return result