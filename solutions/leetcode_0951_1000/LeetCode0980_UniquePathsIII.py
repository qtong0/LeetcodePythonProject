class Solution:
    def uniquePathsIII(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = [0]
        length = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    length += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, res, length)
        return res[0]

    def dfs(self, grid, i, j, res, length):
        if grid[i][j] == 2:
            if length == 0:
                res[0] += 1
            return
        m, n = len(grid), len(grid[0])
        for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            if 0 <= x < m and 0 <= y < n and grid[x][y] in (0, 2):
                orig = grid[x][y]
                if grid[x][y] == 0:
                    grid[x][y] = 4
                self.dfs(grid, x, y, res, length-1)
                grid[x][y] = orig

    def test(self):
        testCases = [
            [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
            [[1,0,0,0],[0,0,0,0],[0,0,0,2]],
            [[0,1],[2,0]],
        ]
        for grid in testCases:
            res = self.uniquePathsIII(grid)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
