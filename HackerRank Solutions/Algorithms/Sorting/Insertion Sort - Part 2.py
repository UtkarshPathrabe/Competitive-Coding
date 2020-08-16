#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        n = arr[i]
        while(i > 0 and n < arr[i-1]):
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = n
        print (' '.join(str(i) for i in arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
