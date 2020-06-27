#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minScore = scores[0]
    minScoreBroken = 0
    maxScore = scores[0]
    maxScoreBroken = 0
    for i in range(1, len(scores)):
        if scores[i] > maxScore:
            maxScore = scores[i]
            maxScoreBroken += 1
        if scores[i] < minScore:
            minScore = scores[i]
            minScoreBroken += 1
    return [maxScoreBroken, minScoreBroken]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
