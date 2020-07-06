#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b) + 1):
        isFactor = True
        isFactorOf = True
        for j in range(len(a)):
            if i%a[j] != 0:
                isFactor = False
                break
        if isFactor:
            for j in range(len(b)):
                if b[j]%i != 0:
                    isFactorOf = False
                    break
            if isFactorOf:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
