#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    result = list(p)
    for i in range(1, len(p) + 1):
        temp = 0
        for j in range(0, len(p)):
            if p[j] == i:
                temp = j+1
                break
        for j in range(0, len(p)):
            if p[j] == temp:
                temp = j+1
                break
        result[i-1] = temp
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
