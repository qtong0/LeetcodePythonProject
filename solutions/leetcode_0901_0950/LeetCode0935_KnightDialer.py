class Solution(object):
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0]*12 for _ in range(n+1)]
        for i in range(10):
            dp[0][i] = 1
            dp[1][i] = 1
        dp[1][10] = dp[1][11] = 0
        for i in range(2, n+1):
            dp[i][1] = (dp[i-1][8]+dp[i-1][6]) % MOD
            dp[i][2] = (dp[i-1][7]+dp[i-1][9]) % MOD
            dp[i][3] = (dp[i-1][4]+dp[i-1][8]) % MOD
            dp[i][4] = (dp[i-1][3]+dp[i-1][9]+dp[i-1][0]) % MOD
            dp[i][5] = 0
            dp[i][6] = (dp[i-1][7]+dp[i-1][0]+dp[i-1][1]) % MOD
            dp[i][7] = (dp[i-1][6]+dp[i-1][2]) % MOD
            dp[i][8] = (dp[i-1][1]+dp[i-1][3]) % MOD
            dp[i][9] = (dp[i-1][4]+dp[i-1][2]) % MOD
            dp[i][10] = 0
            dp[i][0] = (dp[i-1][4]+dp[i-1][6]) % MOD
            dp[i][11] = 0
        res = 0
        for i in range(10):
            res = (res + dp[n][i]) % MOD
        return res



    def test(self):
        testCases = [
            4,
        ]
        for n in testCases:
            res = self.knightDialer(n)
            print('res: %s' % res)
            print('-='*30+'-')



if __name__ == '__main__':
    Solution().test()
