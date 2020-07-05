#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(balls):
    return round(sum(balls) / 2, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    balls_count = int(input())

    balls = []

    for _ in range(balls_count):
        balls_item = int(input())
        balls.append(balls_item)

    result = solve(balls)

    fptr.write(str(result) + '\n')

    fptr.close()
