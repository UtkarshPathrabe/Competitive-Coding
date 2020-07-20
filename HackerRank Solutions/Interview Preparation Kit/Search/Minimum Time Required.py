#!/bin/python3

import math
import os
import random
import re
import sys
from math import ceil
from collections import Counter

# Complete the minTime function below.
def minTime(machines, goal):
    machineTimeCompletionFrequency = Counter(machines)
    fastest = min(machineTimeCompletionFrequency.keys())
    minimumDays = 1
    maximumDays = ceil((fastest * goal) / machineTimeCompletionFrequency[fastest])
    while maximumDays - minimumDays > 1:
        mid = (maximumDays + minimumDays) // 2
        daysTaken = sum((mid // x) * y for x, y in machineTimeCompletionFrequency.items())
        if daysTaken < goal:
            minimumDays = mid
        else:
            maximumDays = mid
    return maximumDays

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
