#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    mapOfDuplets = dict()
    mapOfTriplets = dict()
    count = 0
    for i in arr:
        if i in mapOfTriplets:
            count += mapOfTriplets[i]
        if i in mapOfDuplets:
            if i*r in mapOfTriplets:
                mapOfTriplets[i*r] += mapOfDuplets[i]
            else:
                mapOfTriplets[i*r] = mapOfDuplets[i]
        if i*r in mapOfDuplets:
            mapOfDuplets[i*r] += 1
        else:
            mapOfDuplets[i*r] = 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
