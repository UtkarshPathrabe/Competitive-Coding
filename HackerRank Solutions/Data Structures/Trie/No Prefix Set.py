from collections import defaultdict

def Trie():
    return defaultdict(Trie)

def add(trie, word):
    if word == '':
        if len(trie) > 0: 
            # current word is a prefix of a previous word
            return False
        trie[word] = ''
        return True
    if '' in trie:
        # a prefix of the current word is a previous word
        return False
    return add(trie[word[0]], word[1:])
  
n = int(input())
trie = Trie()
outputPrinted = False
for _ in range(n):
    line = input().strip()
    if not add(trie, line):
        print('BAD SET')
        print(line)
        outputPrinted = True
        break
if not outputPrinted:
    print('GOOD SET')