class Codec:
    
    def __init__(self):
        self.alphabets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.hashMap = {}
        self.key = self._getRand()
        
    def _getRand(self):
        temp = []
        for i in range(6):
            temp.append(random.choice(self.alphabets))
        return ''.join(temp)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while self.key in self.hashMap:
            self.key = self._getRand()
        self.hashMap[self.key] = longUrl
        return 'http://tinyurl.com/' + self.key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashMap[shortUrl.replace('http://tinyurl.com/', '')]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))