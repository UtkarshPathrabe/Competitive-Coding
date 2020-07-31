#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shares = 5
    likes = shares // 2
    cumulativeLikes = likes
    for i in range(1, n):
        shares = likes * 3
        likes = shares // 2
        cumulativeLikes += likes
    return cumulativeLikes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
