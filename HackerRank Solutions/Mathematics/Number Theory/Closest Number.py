#!/bin/python3

import os
import sys
import math

def closestNumber(a, b, x):
    tempNumber = a ** b
    floorNumber = math.floor(tempNumber / x) * x
    ceilNumber = math.ceil(tempNumber / x) * x
    if tempNumber - floorNumber > ceilNumber - tempNumber:
        return ceilNumber
    else:
        return floorNumber

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
