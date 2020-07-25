#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    dataMap = defaultdict(lambda : 0)
    frequencyMap = defaultdict(lambda : 0)
    result = []
    for queryType, value in queries:
        if queryType == 1:
            frequencyMap[dataMap[value]] = max(0, frequencyMap[dataMap[value]] - 1)
            dataMap[value] += 1
            frequencyMap[dataMap[value]] += 1
        elif queryType == 2:
            frequencyMap[dataMap[value]] = max(0, frequencyMap[dataMap[value]] - 1)
            dataMap[value] = max(0, dataMap[value] - 1)
            if dataMap[value] > 0:
                frequencyMap[dataMap[value]] += 1
        elif queryType == 3:
            if frequencyMap[value] > 0:
                result.append(1)
            else:
                result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
