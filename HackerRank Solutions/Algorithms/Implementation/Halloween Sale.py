#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    numberOfGames = 0
    costOfGame = p
    while s - costOfGame >= 0:
        numberOfGames += 1
        s -= costOfGame
        if costOfGame - d >= m:
            costOfGame -= d
        else:
            costOfGame = m
    return numberOfGames

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
