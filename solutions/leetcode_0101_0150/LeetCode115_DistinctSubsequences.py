class Solution(object):
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]


    def test(self):
        testCases= [
            ('rabbbit', 'rabbit'),
            ('abbt', 'abt'),
            ('ABCDE', 'ACE'),
            ('ABCDE', 'AEC'),
        ]
        for s, t in testCases:
            print('s: %s, t: %s' % (s, t))
            result = self.numDistinct(s, t)
            print('result: %s' % (result))
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
