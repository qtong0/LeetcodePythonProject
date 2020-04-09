class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False


class StreamChecker:

    def __init__(self, words):
        self.root = Node(None)
        self.queries = ''
        for word in words:
            node = self.root
            for i, c in enumerate(word[::-1]):
                if c in node.children:
                    newNode = node.children[c]
                else:
                    newNode = Node(c)
                node.children[c] = newNode
                if i == len(word)-1:
                    newNode.isLeaf = True
                node = newNode

    def query(self, letter: str) -> bool:
        node = self.root
        self.queries += letter
        for i in range(len(self.queries)-1, -1, -1):
            c = self.queries[i]
            if c not in node.children:
                return False
            else:
                node = node.children[c]
                if node.isLeaf:
                    return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


if __name__ == '__main__':
    streamChecker = StreamChecker(["cd","f","kl"]); # init the dictionary.
    print(streamChecker.query('a'))          # return false
    print(streamChecker.query('b'))          # return false
    print(streamChecker.query('c'))          # return false
    print(streamChecker.query('d'))          # return true, because 'cd' is in the wordlist
    print(streamChecker.query('e'))          # return false
    print(streamChecker.query('f'))          # return true, because 'f' is in the wordlist
    print(streamChecker.query('g'))          # return false
    print(streamChecker.query('h'))          # return false
    print(streamChecker.query('i'))          # return false
    print(streamChecker.query('j'))          # return false
    print(streamChecker.query('k'))          # return false
    print(streamChecker.query('l'))          # return true, because 'kl' is in the wordlist
