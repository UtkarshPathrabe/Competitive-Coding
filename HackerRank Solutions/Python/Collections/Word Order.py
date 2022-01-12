# Enter your code here. Read input from STDIN. Print output to STDOUT
freqMap = {}
N = int(input())
for i in range(N):
    word = input()
    if word in freqMap:
        freqMap[word] += 1
    else:
        freqMap[word] = 1
print(len(freqMap))
for key, val in freqMap.items():
    print(val, end =" ")