#!/bin/python

import sys
arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
maxSum = -99999
for i in range(1, 5):
    for j in range(1, 5):
        maxSum = max(maxSum, arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1])
print maxSum