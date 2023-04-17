class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arrLength, hashMap, i = len(arr), {}, 0
        for piece in pieces:
            hashMap[piece[0]] = piece
        while i < arrLength:
            if arr[i] in hashMap:
                j, piece = 0, hashMap[arr[i]]
                while j < len(piece) and i < arrLength and piece[j] == arr[i]:
                    j += 1
                    i += 1
                if j != len(piece):
                    return False
            else:
                return False
        return i == arrLength