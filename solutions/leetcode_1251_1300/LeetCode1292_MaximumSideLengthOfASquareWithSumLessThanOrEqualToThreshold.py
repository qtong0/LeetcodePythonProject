class Solution:
    def maxSideLength(self, mat, threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + mat[i][j]
        l, r = 0, min(m, n)
        while l <= r:
            mid = (l+r)//2
            if self.canSplit(dp, mid, threshold):
                l = mid+1
            else:
                r = mid-1
        return max(0, l-1)

    def canSplit(self, dp, length, threshold):
        m, n = len(dp), len(dp[0])
        for i in range(m-length):
            for j in range(n-length):
                sumVal = dp[i+length][j+length]-dp[i][j+length]-dp[i+length][j]+dp[i][j]
                if sumVal <= threshold:
                    return True
        return False

    def test(self):
        testCases = [
            [[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4],
            [[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1],
            [[[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6],
            [[[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184],
        ]
        for mat, threshold in testCases:
            res = self.maxSideLength(mat, threshold)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
