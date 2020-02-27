import random

class Codec:

    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.prefix = 'http://tinyurl.com/'
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2code:
            code = ''.join([random.choice(self.valid_chars) for _ in range(6)])
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return self.prefix + self.url2code[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code2url[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
