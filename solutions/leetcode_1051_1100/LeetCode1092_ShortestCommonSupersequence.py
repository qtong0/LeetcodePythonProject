class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        res, i, j = '', 0, 0
        s = self.lcs(str1, str2)
        for c in s:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i, j = i+1, j+1
        return res + str1[i:] + str2[j:]

    def lcs(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [['']*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + s1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)
        return dp[-1][-1]


    def test(self):
        test_cases = [
            ['abac', 'cab'],
            ['aaaaaaaa', 'aaaaaaaa'],
        ]
        for s1, s2 in test_cases:
            res = self.shortestCommonSupersequence(s1, s2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
