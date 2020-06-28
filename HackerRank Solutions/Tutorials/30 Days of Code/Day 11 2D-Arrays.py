#!/bin/python

import sys
arr = []
for arr_i in xrange(6):
   arr_temp = map(int, raw_input().strip().split(' '))
   arr.append(arr_temp)

max_sum = -9999999
for i in range(1,5):
    for j in range(1,5):
        max_sum = max(arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1], max_sum)

print max_sum