class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        dp = [[0]*arrLen for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1, steps+1):
            for j in range(arrLen):
                dp[i][j] = dp[i-1][j]
                if j+1 < arrLen:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD
                if j-1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
        return dp[-1][0]

    def test(self):
        testCases = [
            [3,2],
            [2,4],
            [4,2],
            [3,3],
            [430,148488],
        ]
        for steps, arrLen in testCases:
            res = self.numWays(steps, arrLen)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
