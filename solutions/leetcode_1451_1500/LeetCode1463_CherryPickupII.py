from typing import List


class Solution:
    # DFS + Memorization
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.memo = {}
        return self.dfs(grid, 0, 0, 0, n-1)

    def dfs(self, grid, i1, j1, i2, j2):
        if (i1, j1, i2, j2) in self.memo:
            return self.memo[(i1, j1, i2, j2)]
        m, n = len(grid), len(grid[0])
        if i1 >= m:
            return 0
        res = 0
        for x1, y1 in (i1+1, j1-1), (i1+1, j1), (i1+1, j1+1):
            for x2, y2 in (i2+1, j2-1), (i2+1, j2), (i2+1, j2+1):
                if 0 <= y1 < n and  0 <= y2 < n:
                    if i1 == i2 and j1 == j2:
                        res = max(res, grid[i1][j1] + self.dfs(grid, x1, y1, x2, y2))
                    else:
                        res = max(res, grid[i1][j1] + grid[i2][j2] + self.dfs(grid, x1, y1, x2, y2))

        self.memo[(i1, j1, i2, j2)] = res
        return res



    def test(self):
        test_cases = [
            [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]],
            # [[3,1,1],[2,5,1],[1,5,5],[2,1,1]],
            # [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]],
            # [[1,1],[1,1]],
        ]
        for grid in test_cases:
            res = self.cherryPickup(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
