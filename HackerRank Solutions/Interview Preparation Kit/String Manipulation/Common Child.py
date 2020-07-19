#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    l1, l2 = len(s1), len(s2)
    CommonChildLength = [[0] * (l2 + 1) for i in range(l1 + 1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                CommonChildLength[i][j] = CommonChildLength[i-1][j-1] + 1
            else:
                CommonChildLength[i][j] = max(CommonChildLength[i-1][j], CommonChildLength[i][j-1])
    return CommonChildLength[l1][l2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
