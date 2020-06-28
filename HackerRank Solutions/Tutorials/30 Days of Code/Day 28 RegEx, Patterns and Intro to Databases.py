#!/bin/python
import sys
import re
N = int(raw_input().strip())
List = []
for a0 in xrange(N):
    firstName, emailID = raw_input().strip().split(' ')
    firstName, emailID = [str(firstName),str(emailID)]
    searchObj = re.search(r'[a-z]*@gmail.com', emailID)
    if searchObj:
        List.append(firstName)
List.sort()
for item in List:
    print item