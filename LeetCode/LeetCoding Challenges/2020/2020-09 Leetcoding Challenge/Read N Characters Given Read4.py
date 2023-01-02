"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

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
        