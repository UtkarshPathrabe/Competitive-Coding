class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, seen, lastOccurence = deque([]), set(), {char: index for index, char in enumerate(s)}
        for index, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and index < lastOccurence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)