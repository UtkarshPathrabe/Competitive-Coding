class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.tree = [0] * (self.size * 2)
        for i in range(self.size, 2 * self.size):
            self.tree[i] = nums[i - self.size]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i: int, val: int) -> None:
        position = i + self.size
        self.tree[position] = val
        while position > 0:
            left = right = position
            if position % 2 == 0:
                right = position + 1
            else:
                left = position - 1
            self.tree[position // 2] = self.tree[left] + self.tree[right]
            position //= 2

    def sumRange(self, l: int, r: int) -> int:
        l, r, currentSum = l + self.size, r + self.size, 0
        while l <= r:
            if l % 2 == 1:
                currentSum += self.tree[l]
                l += 1
            if r % 2 == 0:
                currentSum += self.tree[r]
                r -= 1
            l, r = l // 2, r // 2
        return currentSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)