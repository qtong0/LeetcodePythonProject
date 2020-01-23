class Solution:
    def spellchecker(self, wordlist, queries):
        res = []
        hashmap = {}
        for w in queries:
            res.append(self.match(wordlist, w, hashmap))
        return res

    def match(self, wordList, word, hashmap):
        if word in hashmap:
            return hashmap[word]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        resCap = ''
        resVowel = ''
        for word0 in wordList:
            if word0 == word:
                return word
            if len(word0) == len(word):
                resCap0, resVowel0 = '', ''
                for c0, c1 in zip(word0, word):
                    if c0 == c1 or c0.lower() == c1.lower():
                        resCap0 += c0
                        resVowel0 += c0
                    elif c0.lower() in vowels and c1.lower() in vowels:
                        resVowel0 += c0
                    else:
                        resCap0, resVowel0 = '', ''
                if len(resCap0) == len(word0) and not resCap:
                    resCap = resCap0
                elif len(resVowel0) == len(word0) and not resVowel:
                    resVowel = resVowel0
        if resCap:
            hashmap[word] = resCap
            return resCap
        if resVowel:
            hashmap[word] = resVowel
            return resVowel
        hashmap[word] = ''
        return ''

    def test(self):
        testCases = [
            [
                ["KiTe","kite","hare","Hare"],
                ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"],
            ],
            [
                ["YellOw"],
                ["yollow"],
            ],
        ]
        for wordList, queries in testCases:
            res = self.spellchecker(wordList, queries)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
