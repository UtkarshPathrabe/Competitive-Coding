#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    countOfDivisors = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit != 0 and n % digit == 0:
            countOfDivisors += 1
        temp = temp // 10
    return countOfDivisors

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
