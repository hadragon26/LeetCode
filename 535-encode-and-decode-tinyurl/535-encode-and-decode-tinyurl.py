class Codec:
    
    def __init__(self):
        self.e = {}
        self.p ={}
        self.code = 1 

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.e[longUrl] = self.code
        self.p[self.code] = longUrl
        self.code+=1
        
        return self.e[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.p[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))