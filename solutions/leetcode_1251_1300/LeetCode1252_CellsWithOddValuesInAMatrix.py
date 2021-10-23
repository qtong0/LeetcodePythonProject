from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0]*m
        cols = [0]*n
        mat = [[0]*n for _ in range(m)]
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
            mat[i][j] += 2
        res = 0
        for i in range(m):
            for j in range(n):
                val = mat[i][j] + rows[i] + cols[j]
                if val % 2 != 0:
                    res += 1
        return res


    def test(self):
        test_cases = [
            [2, 3, [[0,1],[1,1]]],
            [2, 2, [[1,1],[0,0]]],
        ]
        for m, n, indices in test_cases:
            res = self.oddCells(m, n, indices)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
