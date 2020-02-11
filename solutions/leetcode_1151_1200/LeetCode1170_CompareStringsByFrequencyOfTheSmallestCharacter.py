import bisect


class Solution:
    def numSmallerByFrequency(self, queries, words):
        counts = []
        for word in words:
            count = self.f(word)
            idx = bisect.bisect_left(counts, count)
            counts.insert(idx, count)
        res = []
        for s in queries:
            count = self.f(s)
            idx = bisect.bisect_right(counts, count)
            res.append(len(words)-idx)
        return res

    def f(self, s):
        dp = [0]*26
        minC = 'z'
        for c in s:
            dp[ord(c)-ord('a')] += 1
            minC = min(minC, c)
        return dp[ord(minC)-ord('a')]

    def test(self):
        testCases = [
            [
                ["cbd"],
                ["zaaaz"],
            ],
            [
                ["bbb","cc"],
                ["a","aa","aaa","aaaa"],
            ],
        ]
        for queries, words in testCases:
            res = self.numSmallerByFrequency(queries, words)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
