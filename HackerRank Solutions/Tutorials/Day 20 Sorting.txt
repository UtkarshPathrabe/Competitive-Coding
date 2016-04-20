#!/bin/python
import sys
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
i, numberOfSwaps = 0, 0
while i < n:
    j = 0
    while j < n-1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
        j += 1
    if numberOfSwaps == 0:
        break
    i += 1
print 'Array is sorted in ' + str(numberOfSwaps) + ' swaps.'
print 'First Element: ' + str(a[0])
print 'Last Element: ' + str(a[n-1])