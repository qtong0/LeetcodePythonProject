class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        res = [None]*n
        index = list(range(n))
        for card in sorted(deck):
            res[index.pop(0)] = card
            if index:
                index.append(index.pop(0))
        return res

    def test(self):
        testCases = [
            [17,13,11,2,3,5,7],
        ]
        for deck in testCases:
            res = self.deckRevealedIncreasing(deck)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
