class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j])+1
                else:
                    dp[i+1][j+1] = 0
                res += dp[i+1][j+1]
        return res

    def test(self):
        test_cases = [
            [
                [0,1,1,1],
                [1,1,1,1],
                [0,1,1,1]
            ],
            [
                [1,0,1],
                [1,1,0],
                [1,1,0]
            ],
        ]
        for matrix in test_cases:
            res = self.countSquares(matrix)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
