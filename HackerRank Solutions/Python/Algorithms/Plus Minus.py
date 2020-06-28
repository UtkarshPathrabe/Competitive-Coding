#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveNumbers = 0
    negativeNumbers = 0
    zeroes = 0
    totalNumbers = len(arr)
    for i in arr:
        if i > 0:
            positiveNumbers += 1
        elif i < 0:
            negativeNumbers += 1
        else:
            zeroes += 1
    print(positiveNumbers / totalNumbers)
    print(negativeNumbers / totalNumbers)
    print(zeroes / totalNumbers)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
