class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        nums = [[(num >> i) & 1 for i in range(L)][::-1] for num in nums]
        maxXor, trie = 0, {}
        for num in nums:
            currentNode, xorNode, currentXor = trie, trie, 0
            for bit in num:
                currentNode = currentNode.setdefault(bit, {})
                toggledBit = 1 - bit
                if toggledBit in xorNode:
                    currentXor = (currentXor << 1) | 1
                    xorNode = xorNode[toggledBit]
                else:
                    currentXor = currentXor << 1
                    xorNode = xorNode[bit]
            maxXor = max(maxXor, currentXor)
        return maxXor