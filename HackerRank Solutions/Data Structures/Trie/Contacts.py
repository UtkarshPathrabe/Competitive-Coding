#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
def contacts(queries):
    contactMap = dict()
    result = list()
    for query in queries:
        if query[0] == 'add':
            for i in range(1, len(query[1]) + 1):
                subString = query[1][:i]
                if subString in contactMap:
                    contactMap[subString] += 1
                else:
                    contactMap[subString] = 1
        else:
            if query[1] in contactMap:
                result.append(contactMap[query[1]])
            else:
                result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
