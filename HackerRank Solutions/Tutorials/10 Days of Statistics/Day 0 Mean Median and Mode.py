import numpy
from scipy import stats

N = int(input())
X = list(map(int, input().strip().split()))

print(numpy.mean(X))
print(numpy.median(X))
print(stats.mode(X)[0][0])