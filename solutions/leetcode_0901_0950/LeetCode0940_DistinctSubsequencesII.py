class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1]*2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i
        return (dp[-1]-1) % (10**9+7)

    def test(self):
        testCases = [
            'abc',
            'aba',
            'aaa',
        ]
        for s in testCases:
            res = self.distinctSubseqII(s)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
