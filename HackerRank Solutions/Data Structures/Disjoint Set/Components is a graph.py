#!/bin/python3

import os
import sys

def componentsInGraph(queries):
    def findSet(rootArray, i):
        if rootArray[i] == i:
            return i
        else:
            return findSet(rootArray, rootArray[i])
    n = len(queries)
    N = 2 * n + 1
    rootArray = [i for i in range(N)]
    connectedComponentCountArray = [1] * N
    for query in queries:
        gRoot = findSet(rootArray, int(query[0]))
        bRoot = findSet(rootArray, int(query[1]))
        if gRoot != bRoot:
            rootArray[bRoot] = gRoot
            connectedComponentCountArray[gRoot] += connectedComponentCountArray[bRoot]
            connectedComponentCountArray[bRoot] = 0
    minValue = sys.maxsize
    maxValue = 0
    print(connectedComponentCountArray)
    for i in connectedComponentCountArray:
        if i > 1 and i < minValue:
            minValue = i
        if i > maxValue:
            maxValue = i
    return [minValue, maxValue]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
