#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    subsetSum = list(arr)
    for i in range(1, len(arr)):
        if i == 1:
            subsetSum[1] = max(subsetSum[0], subsetSum[1])
        else:
            subsetSum[i] = max([subsetSum[i], subsetSum[i-1], subsetSum[i-2] + subsetSum[i]])
    return subsetSum[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
