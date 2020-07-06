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

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def gcdOfList(X):
    g = X[0]
    for i in range(1, len(X)):
        g = gcd(g, X[i])
    return g

def lcm(a, b):
    return (a * b) / gcd(a, b)

def lcmOfList(X):
    l = X[0]
    for i in range(1, len(X)):
        l = lcm(l, X[i])
    return l

def getTotalX(a, b):
    l = lcmOfList(a)
    g = gcdOfList(b)
    count = 0
    i = l
    j = 2
    while(i <= g):
        if (g % i == 0):
            count += 1
        i = l*j
        j += 1
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
