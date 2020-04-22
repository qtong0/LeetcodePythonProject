class Solution:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        if not A: return 0
        n = len(A)
        dp = [0]*n
        for i in range(n):
            curMax = 0
            for j in range(1, min(K, i+1) + 1):
                curMax = max(curMax, A[i-j+1])
                if i >= j:
                    dp[i] = max(dp[i], dp[i-j] + curMax*j)
                else:
                    dp[i] = max(dp[i], curMax*j)
        return dp[-1]

    def test(self):
        testCases = [
            [[1,15,7,9,2,5,10], 3],
        ]
        for arr, k in testCases:
            res = self.maxSumAfterPartitioning(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
