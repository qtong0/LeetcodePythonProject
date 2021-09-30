class Solution(object):
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k+maxPts:
            return 1
        dp = [1.0] + [0.0]*n
        sumPos = 1.0
        for i in range(1, n+1):
            dp[i] = sumPos / maxPts
            if i < k:
                sumPos += dp[i]
            if i - maxPts >= 0:
                sumPos -= dp[i-maxPts]
        return sum(dp[k:])

    def test(self):
        testCases = [
            [10, 1, 10],
            [6, 1, 10],
            [21, 17, 10],
        ]
        for n, k, w in testCases:
            result = self.new21Game(n, k, w)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
