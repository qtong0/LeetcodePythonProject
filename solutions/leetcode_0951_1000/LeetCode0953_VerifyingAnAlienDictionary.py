class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hashmap = {}
        for i, c in enumerate(order):
            hashmap[c] = i
        for i in range(1, len(words)):
            pword = words[i-1]
            word = words[i]
            j = 0
            while j < len(pword) and j < len(word) and pword[j] == word[j]:
                j += 1
            if j == len(word) and j < len(pword):
                return False
            if j < len(pword) and j < len(word) and hashmap[pword[j]] > hashmap[word[j]]:
                return False
        return True

    def test(self):
        testCases = [
            [
                ["hello","leetcode"],
                "hlabcdefgijkmnopqrstuvwxyz"
            ],
        ]
        for words, order in testCases:
            res = self.isAlienSorted(words, order)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
