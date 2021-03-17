from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'append':
        d.append(cmd[1])
    elif cmd[0] == 'appendleft':
        d.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        d.pop()
    elif cmd[0] == 'popleft':
        d.popleft()
print(' '.join(d))