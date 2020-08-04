#!/bin/python3

import os
import sys

#
# Complete the cookies function below.
#
def cookies(k, A):
    from heapq import heappush, heappop, heapify
    heapify(A)
    operationCount = 0
    while A[0] < k and len(A) > 1:
        heappush(A, heappop(A) + 2*heappop(A))
        operationCount += 1
    return operationCount if A[0] >= k else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
