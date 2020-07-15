#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(heights):
    maxArea = 0
    for i in range(0, len(heights)):
        leftIndexWithValidHeight = i
        while leftIndexWithValidHeight > 0:
            if heights[leftIndexWithValidHeight - 1] < heights[i]:
                break
            leftIndexWithValidHeight -= 1
        rightIndexWithValidHeight = i
        while rightIndexWithValidHeight < len(heights) - 1:
            if heights[rightIndexWithValidHeight + 1] < heights[i]:
                break
            rightIndexWithValidHeight += 1
        area = heights[i] * (rightIndexWithValidHeight - leftIndexWithValidHeight + 1)
        if area > maxArea:
            maxArea = area
    return maxArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
