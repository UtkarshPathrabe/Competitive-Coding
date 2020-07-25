#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for subStringLength in range(1, len(s) + 1):
        a = ["".join(sorted(s[i : i + subStringLength])) for i in range(len(s) - subStringLength + 1)]
        b = Counter(a)
        for i in b:
            count += (b[i] * (b[i] - 1)) // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
