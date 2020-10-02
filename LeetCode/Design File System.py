class FileSystem:

    def __init__(self):
        self.fileSystem = {}
        self.endToken = '#'

    def createPath(self, path: str, value: int) -> bool:
        if path in {'', '/'}:
            return False
        if path.startswith('/'):
            tokens = path.split('/')[1:]
            currentNode = self.fileSystem
            for i, token in enumerate(tokens, 1):
                if token not in currentNode:
                    if i != len(tokens):
                        return False
                    else:
                        currentNode[token] = {self.endToken: value}
                        return True
                else:
                    currentNode = currentNode[token]
        return False

    def get(self, path: str) -> int:
        if path in {'', '/'}:
            return -1
        if path.startswith('/'):
            tokens = path.split('/')[1:]
            currentNode = self.fileSystem
            for i, token in enumerate(tokens, 1):
                if token not in currentNode:
                    return -1
                else:
                    currentNode = currentNode[token]
                    if i == len(tokens) and self.endToken in currentNode:
                        return currentNode[self.endToken]
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)