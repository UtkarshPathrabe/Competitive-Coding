class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic, count = {}, 0
        for a in arr:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        for key, val in dic.items():
            if val == 1:
                count += 1
                if count == k:
                    return key
        return ''