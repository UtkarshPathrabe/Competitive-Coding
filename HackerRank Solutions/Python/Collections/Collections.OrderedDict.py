from collections import OrderedDict
N = input()
ordDict = OrderedDict()
for i in range(int(N)):
    item, cost = input().rsplit(' ', 1)
    if item in ordDict:
        ordDict[item] += int(cost)
    else:
        ordDict[item] = int(cost)
for k, v in ordDict.items():
    print(k, v)