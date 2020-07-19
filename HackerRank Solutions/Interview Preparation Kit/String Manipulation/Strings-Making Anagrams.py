#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    frequency = [0] * 26
    for i in a:
        frequency[ord(i) - ord('a')] += 1
    for i in b:
        frequency[ord(i) - ord('a')] -= 1
    deletionsRequired = 0
    for i in frequency:
        deletionsRequired += abs(i)
    return deletionsRequired

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
