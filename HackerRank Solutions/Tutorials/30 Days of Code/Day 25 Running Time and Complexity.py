import math
for test in range(int(raw_input().strip())):
    N = int(raw_input().strip())
    flag = True
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            flag = False
            break
    if flag and N > 1:
        print 'Prime'
    else:
        print 'Not prime'