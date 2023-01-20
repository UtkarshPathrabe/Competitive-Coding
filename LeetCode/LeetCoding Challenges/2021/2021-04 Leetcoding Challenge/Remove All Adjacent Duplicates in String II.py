class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l, stack, i = list(s), [], 0
        while i < len(l):
            if i == 0 or l[i] != l[i - 1]:
                stack.append(1)
            else:
                count = stack.pop() + 1
                if count == k:
                    l = l[:i - k + 1] + l[i + 1:]
                    i = i - k
                else:
                    stack.append(count)
            i += 1
        return ''.join(l)