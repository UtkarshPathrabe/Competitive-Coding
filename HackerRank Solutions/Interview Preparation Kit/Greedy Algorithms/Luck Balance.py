#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance():
    n, k = list(map(int, input().strip().split()))
    luckSum = 0
    importantContestsLuck = []
    for _ in range(n):
        luck, importance = list(map(int, input().strip().split()))
        if importance:
            importantContestsLuck.append(luck)
        else:
            luckSum += luck
    importantContestsLuck.sort(reverse=True)
    for i in range(len(importantContestsLuck)):
        if i < k:
            luckSum += importantContestsLuck[i]
        else:
            luckSum -= importantContestsLuck[i]
    return luckSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = luckBalance()

    fptr.write(str(result) + '\n')

    fptr.close()
