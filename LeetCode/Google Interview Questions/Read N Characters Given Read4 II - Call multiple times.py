# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    
    def __init__(self):
        self.__buffer = ['\0'] * 4
        self.__bufferSize = 0
        self.__bufferOffset = 0
        
    def __readOne(self, buf: List[str], index: int) -> bool:
        if self.__bufferSize == 0 or self.__bufferSize == self.__bufferOffset:
            self.__bufferSize = read4(self.__buffer)
            self.__bufferOffset = 0
        if self.__bufferSize == 0:
            return False
        buf[index] = self.__buffer[self.__bufferOffset]
        self.__bufferOffset += 1
        return True
    
    def read(self, buf: List[str], n: int) -> int:
        charactersRead = 0
        while charactersRead < n and self.__readOne(buf, charactersRead):
            charactersRead += 1
        return charactersRead