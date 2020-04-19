class Node:
    def __init__(self, val):
        self.val = val
        self.arr = []
        self.idx = -1
        self.children = {}


class Solution:
    # O (k^2 * N)
    def palindromePairs(self, words):
        self.root = Node(None)
        for i, word in enumerate(words):
            self.build(word, i)
        res = []
        for i, word, in enumerate(words):
            self.search(word, res, i)
        return res

    def build(self, word, i):
        node = self.root
        for j in range(len(word)-1, -1, -1):
            c = word[j]
            if c not in node.children:
                node.children[c] = Node(c)
            if self.isPalindrome(word, 0, j):
                node.arr.append(i)
            node = node.children[c]
        node.arr.append(i)
        node.idx = i

    def search(self, word, res, i):
        node = self.root
        for j, c in enumerate(word):
            if node.idx >= 0 and node.idx != i and self.isPalindrome(word, j, len(word)-1):
                res.append([i, node.idx])
            if c not in node.children:
                return
            node = node.children[c]
        for j in node.arr:
            if i == j:
                continue
            res.append([i, j])

    def isPalindrome(self, word, l, r):
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

    def test(self):
        testCases = [
            ["abcd", "dcba", "lls", "s", "sssll"],
        ]
        for words in testCases:
            print('words: %s' % (words))
            result = self.palindromePairs(words)
            print('result: %s' % (result))
            print('-='*20+'-')


class Solution_ANOTHER(object):
    # O (k^2 * N)
    def palindromePairs(self, words):
        if not words: return []
        hashmap = {}
        result = []
        for i, word in enumerate(words):
            hashmap[word] = i
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                s1 = word[:j]
                s2 = word[j:]
                if self.isPalindrome(s1):
                    str2rvs = s2[::-1]
                    if str2rvs in hashmap and hashmap[str2rvs] != i:
                        result.append([hashmap[str2rvs], i])
                if self.isPalindrome(s2):
                    str1rvs = s1[::-1]
                    if str1rvs in hashmap and hashmap[str1rvs] != i and s2:
                        result.append([i, hashmap[str1rvs]])
        return result
    
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
    
    def test(self):
        testCases = [
            ["bat", "tab", "cat"],
            ["abcd", "dcba", "lls", "s", "sssll"],
        ]
        for words in testCases:
            print('words: %s' % (words))
            result = self.palindromePairs(words)
            print('result: %s' % (result))
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
