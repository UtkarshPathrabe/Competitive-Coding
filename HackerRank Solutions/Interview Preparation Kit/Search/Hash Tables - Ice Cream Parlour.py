#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    pricesMap = dict()
    for index, value in enumerate(cost, 1):
        if money-value in pricesMap:
            print(pricesMap[money-value], index)
        pricesMap[value] = index

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
