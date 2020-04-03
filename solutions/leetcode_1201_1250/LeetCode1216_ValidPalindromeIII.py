class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[1]*n for _ in range(n)]
        maxLen = 1
        for i in range(n):
            for j in range(i, -1, -1):
                if j+2 <= i and s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1]+2
                elif j+1 == i and s[i] == s[j]:
                    dp[i][j] = 2
                elif j+1 <= i:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
                maxLen = max(maxLen, dp[i][j])
        return maxLen + k >= n

    def test(self):
        testCases = [
            ["abcdeca", 2],
        ]
        for s, k in testCases:
            res = self.isValidPalindrome(s, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
