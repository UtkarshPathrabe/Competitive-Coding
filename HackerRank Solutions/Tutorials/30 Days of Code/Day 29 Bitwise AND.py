#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = (int(n), int(k))
    a = k - 1
    b = (~a) & -(~a)
    if (a | b) > n:
        print (a - 1)
    else:
        print (a)