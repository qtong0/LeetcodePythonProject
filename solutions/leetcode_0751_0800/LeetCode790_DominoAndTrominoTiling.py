class Solution(object):
    def numTilings(self, N: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 0, 0, 0]
        for _ in range(N):
            ndp = [0, 0, 0, 0]
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD
            ndp[0b10] = (dp[0b00] + dp[0b01]) % MOD
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % MOD
            dp = ndp
        return dp[0]


    def numTilings_another(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 10**9+7
        p3 = -1
        p2 = 0
        p1 = 1
        for _ in range(N):
            cur = (p1*2+p3)%mod
            p3 = p2
            p2 = p1
            p1 = cur
        return p1
    
    def test(self):
        testCases = [
            3,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.numTilings(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
