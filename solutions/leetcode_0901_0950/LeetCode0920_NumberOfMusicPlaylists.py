class Solution(object):
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0]*(n+1) for _ in range(goal+1)]
        dp[0][0] = 1
        for i in range(1, goal+1):
            for j in range(1, n+1):
                dp[i][j] += dp[i-1][j-1]*(n-j+1)
                dp[i][j] += dp[i-1][j]*max(j-k, 0)
                dp[i][j] %= MOD
        return dp[goal][n]


    def test(self):
        testCases = [
            [1, 3, 0],
            [3, 3, 1],
            [2, 3, 0],
            [2, 3, 1],
        ]
        for n, l, k in testCases:
            res = self.numMusicPlaylists(n, l, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
