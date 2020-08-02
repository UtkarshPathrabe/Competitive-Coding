#!/bin/python3

import os
import sys
from collections import defaultdict
import bisect

# Complete the solve function below.
class Node():
    def __init__(self, size, parent=None):
        self.size = size
        self.parent = parent

def sortByWeight(e):
    return e[2]

def solve(tree, queries):
    tree.sort(key=sortByWeight)
    clusters = {i: Node(1) for i in range(1, len(tree) + 2)}
    counts = defaultdict(int)
    for U, V, W in tree:
        uNode = clusters[U]
        vNode = clusters[V]
        while uNode.parent:
            uNode = uNode.parent
        while vNode.parent:
            vNode = vNode.parent
        counts[W] += (uNode.size * vNode.size)
        newNode = Node(uNode.size + vNode.size)
        uNode.parent = newNode
        vNode.parent = newNode
        clusters[U] = newNode
        clusters[V] = newNode
    sortedCountKeys = sorted(counts)
    sortedCounts = [counts[i] for i in sortedCountKeys]
    cumulativeSortedCounts = [0]
    cumulativeSum = 0
    for count in sortedCounts:
        cumulativeSum += count
        cumulativeSortedCounts.append(cumulativeSum)
    result = []
    for query in queries:
        L = bisect.bisect_left(sortedCountKeys, int(query[0]))
        R = bisect.bisect_right(sortedCountKeys, int(query[1]))
        result.append(cumulativeSortedCounts[R] - cumulativeSortedCounts[L])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    tree = []

    for _ in range(n-1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
