from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0]*n for _ in range(m)]
        preSums = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                preSums[i+1][j+1] = preSums[i][j+1] + preSums[i+1][j] + mat[i][j] - preSums[i][j]
        for i in range(m):
            for j in range(n):
                i1, j1 = max(0, i-k), max(0, j-k)
                i2, j2 = min(m, i+k+1), min(n, j+k+1)
                res[i][j] = preSums[i2][j2] - preSums[i1][j2] - preSums[i2][j1] + preSums[i1][j1]
        return res



    def test(self):
        test_cases = [
            [[[1,2,3],[4,5,6],[7,8,9]], 1],
            [[[1,2,3],[4,5,6],[7,8,9]], 2],
        ]
        for mat, k in test_cases:
            res = self.matrixBlockSum(mat, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
