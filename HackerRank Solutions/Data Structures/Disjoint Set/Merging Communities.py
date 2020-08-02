import os
import sys

def findSet(rootArray, i):
    if rootArray[i] != i:
        rootArray[i] = findSet(rootArray, rootArray[i])
    return rootArray[i]

N, Q = list(map(int, input().strip().split()))
rootArray = [i for i in range(N+1)]
connectedComponentCountArray = [1] * (N+1)
for _ in range(Q):
    query = input().strip().split()
    if query[0] == 'M':
        aRoot = findSet(rootArray, int(query[1]))
        bRoot = findSet(rootArray, int(query[2]))
        if aRoot != bRoot:
            rootArray[bRoot] = aRoot
            connectedComponentCountArray[aRoot] += connectedComponentCountArray[bRoot]
            connectedComponentCountArray[bRoot] = 0
    elif query[0] == 'Q':
        print(connectedComponentCountArray[findSet(rootArray, int(query[1]))])