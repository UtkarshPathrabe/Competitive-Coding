from heapq import heappush, heappop

heap = []
itemLookup = set()

def addToHeap(value):
    heappush(heap, value)
    itemLookup.add(value)

def deleteFromHeap(value):
    itemLookup.discard(value)

def minimumFromHeap():
    while heap[0] not in itemLookup:
        heappop(heap)
    print(heap[0])

numberOfQueries = int(input())
for _ in range(numberOfQueries):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
        addToHeap(query[1])
    elif query[0] == 2:
        deleteFromHeap(query[1])
    else:
        minimumFromHeap()