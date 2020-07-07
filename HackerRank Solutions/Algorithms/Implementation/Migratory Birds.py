#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    frequencyArray = [0] * 5
    for i in range(len(arr)):
        frequencyArray[arr[i]-1] += 1
    maxFrequency = frequencyArray[0]
    maxFrequencyBird = 1
    for i in range(1, len(frequencyArray)):
        if frequencyArray[i] > maxFrequency:
            maxFrequency = frequencyArray[i]
            maxFrequencyBird = i+1
    return maxFrequencyBird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
