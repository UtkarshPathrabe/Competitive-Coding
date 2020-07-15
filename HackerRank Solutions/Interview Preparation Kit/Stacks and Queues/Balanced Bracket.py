#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for i in s:
        if i == '{' or i == '[' or i == '(':
            stack.append(i)
        elif i == '}':
            size = len(stack)
            if size == 0 or stack[size-1] != '{':
                return 'NO'
            stack.pop()
        elif i == ']':
            size = len(stack)
            if size == 0 or stack[size-1] != '[':
                return 'NO'
            stack.pop()
        elif i == ')':
            size = len(stack)
            if size == 0 or stack[size-1] != '(':
                return 'NO'
            stack.pop()
    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
