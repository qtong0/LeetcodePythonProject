class Solution:
    def longestArithSeqLength(self, A) -> int:
        if not A: return 0
        n = len(A)
        dp = [{} for _ in range(n)]
        maxLen = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = A[j] - A[i]
                dp[j][diff] = dp[i].get(diff, 0) + 1
                maxLen = max(maxLen, dp[j][diff]+1)
        return maxLen

    def test(self):
        testCases = [
            [3,6,9,12],
            [9,4,7,2,10],
            [20,1,15,3,10,5,8],
            [83,20,17,43,52,78,68,45],
        ]
        for arr in testCases:
            res = self.longestArithSeqLength(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
