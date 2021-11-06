from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = {}
        cols = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] = rows.get(i, 0) + 1
                    cols[j] = cols.get(j, 0) + 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if rows[i] > 1 or cols[j] > 1:
                        res += 1
        return res


    def test(self):
        test_cases = [
            [[1,0],[0,1]],
            [[1,0],[1,1]],
            [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]],
        ]
        for grid in test_cases:
            res = self.countServers(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
