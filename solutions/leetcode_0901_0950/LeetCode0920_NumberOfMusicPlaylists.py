class Solution(object):
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0]*(n+1) for _ in range(goal+1)]
        dp[0][0] = 1
        for i in range(1, goal+1):
            for j in range(1, n+1):
                # (the last added one is new song):
                # listen i - 1 songs with j - 1 different songs
                # then the last one is definitely new song with the choices of N - (j - 1).
                dp[i][j] += dp[i-1][j-1]*(n - (j - 1))
                # (the last added one is old song):
                # listen i - 1 songs with j different songs
                # then the last one is definitely old song with the choices of j
                if j > k:
                    dp[i][j] += dp[i-1][j] * (j - k)
                dp[i][j] %= MOD
        return dp[goal][n]


    def test(self):
        test_cases = [
            [1, 3, 0],
            [3, 3, 1],
            [2, 3, 0],
            [2, 3, 1],
        ]
        for n, l, k in test_cases:
            res = self.numMusicPlaylists(n, l, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
