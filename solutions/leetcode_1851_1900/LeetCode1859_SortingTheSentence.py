class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        arr = [''] * len(words)
        for w in words:
            new_word, idx = self.parseWord(w)
            arr[idx-1] = new_word
        return ' '.join(arr)

    def parseWord(self, word):
        i = len(word)-1
        while i >= 0 and word[i].isdigit():
            i -= 1
        return word[:i+1], int(word[i+1:])

    def test(self):
        test_cases = [
            'is2 sentence4 This1 a3',
            'Myself2 Me1 I4 and3',
        ]
        for s in test_cases:
            res = self.sortSentence(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
