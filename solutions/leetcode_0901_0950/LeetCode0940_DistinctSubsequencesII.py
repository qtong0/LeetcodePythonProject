class Solution(object):
    # example:
    # Input: "aba"
    # Current parsed: "ab"
    #
    # endswith 'a': ["a"]
    # endswith 'b': ["ab","b"]
    #
    # "a" -> "aa"
    # "ab" -> "aba"
    # "b" -> "ba"
    # "" -> "a"
    def distinctSubseqII(self, s: str) -> int:
        ends_with = [0] * 26
        for c in s:
            ends_with[ord(c) - ord('a')] = sum(ends_with) + 1
        return sum(ends_with) % (10**9+7)

    # another solution
    def distinctSubseqII_another(self, s: str) -> int:
        dp = [1]
        last = {}
        for i, c in enumerate(s):
            dp.append(dp[-1]*2)
            if c in last:
                dp[-1] -= dp[last[c]]
            last[c] = i
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
