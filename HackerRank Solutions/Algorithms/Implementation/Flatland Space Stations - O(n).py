#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    spaceStationAt = [0] * n
    for i in c:
        spaceStationAt[i] = 1
    distanceFromLeft = [0] * n
    for i in range(n):
        if spaceStationAt[i] == 1:
            distanceFromLeft[i] = 0
        else:
            if i == 0:
                distanceFromLeft[i] = float('inf')
            else:
                distanceFromLeft[i] = distanceFromLeft[i - 1] + 1
    distanceFromRight = [0] * n
    for i in range(n - 1, -1, -1):
        if spaceStationAt[i] == 1:
            distanceFromRight[i] = 0
        else:
            if i == n-1:
                distanceFromRight[i] = float('inf')
            else:
                distanceFromRight[i] = distanceFromRight[i + 1] + 1
    distance = 0
    for i in range(n):
        distance = max(distance, min(distanceFromLeft[i], distanceFromRight[i]))
    return distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
