class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, d+1):
            dp1 = [0]*(target+1)
            for j in range(1, f+1):
                for k in range(j, target+1):
                    dp1[k] = (dp1[k] + dp[k-j]) % MOD
            dp = dp1
        return dp[-1]

    def test(self):
        test_cases = [
            [1, 6, 3],
            [2, 6, 7],
            [2, 5, 10],
            [1, 2, 3],
            [30, 30, 500],
        ]
        for d, f, target in test_cases:
            res = self.numRollsToTarget(d, f, target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
