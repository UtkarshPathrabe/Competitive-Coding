#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    countOfTriplets, aIndex, bIndex, cIndex = 0, 0, 0, 0
    while bIndex < len(b):
        while aIndex < len(a) and a[aIndex] <= b[bIndex]:
            aIndex += 1
        while cIndex < len(c) and c[cIndex] <= b[bIndex]:
            cIndex += 1
        countOfTriplets += (aIndex * cIndex)
        bIndex += 1
    return countOfTriplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
