class TrieNode:
    
    def __init__(self, string = '', times = 0):
        self.string = string
        self.times = times
        self.children = defaultdict(TrieNode)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.currentString = ''
        for sentence, frequency in zip(sentences, times):
            self.__insert(self.root, sentence, frequency)
    
    def __insert(self, currentNode, sentence, frequency):
        for char in sentence:
            currentNode = currentNode.children.setdefault(char, TrieNode(char))
        currentNode.times += frequency
        
    def __lookup(self, currentNode, string):
        for char in string:
            if char not in currentNode.children:
                return []
            currentNode = currentNode.children[char]
        matchingStrings = []
        self.__traverse(currentNode, string, matchingStrings)
        return matchingStrings
    
    def __traverse(self, currentNode, string, matchingStrings):
        if currentNode.times > 0:
            matchingStrings.append((string, currentNode.times))
        for key in currentNode.children:
            self.__traverse(currentNode.children[key], string + key, matchingStrings)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.__insert(self.root, self.currentString, 1)
            self.currentString = ''
        else:
            self.currentString += c
            listOfTuple = self.__lookup(self.root, self.currentString)
            listOfTuple.sort(key = lambda x : (-1 * x[1], x[0]))
            result = []
            numberOfResults = 0
            for Tuple in listOfTuple:
                result.append(Tuple[0])
                numberOfResults += 1
                if numberOfResults >= 3:
                    break
            return result


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)