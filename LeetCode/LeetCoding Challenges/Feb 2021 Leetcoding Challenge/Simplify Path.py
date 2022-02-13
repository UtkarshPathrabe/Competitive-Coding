class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = deque([])
        for part in parts:
            if part in ['', '.']:
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)