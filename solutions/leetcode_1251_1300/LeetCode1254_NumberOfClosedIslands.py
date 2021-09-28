from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if self.bfs(grid, i, j):
                        res += 1
        return res

    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        queue = [[i, j]]
        reach_border = False
        while queue:
            x, y = queue.pop(0)
            grid[x][y] = -1
            if x in [0, m-1] or y in [0, n-1]:
                reach_border = True
            for x1, y1 in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 0:
                    queue.append([x1, y1])
        return not reach_border

    def test(self):
        test_cases = [
            [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]],
            [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]],
        ]
        for grid in test_cases:
            res = self.closedIsland(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
