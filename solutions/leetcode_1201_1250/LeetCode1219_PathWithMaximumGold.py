class Solution:
    def getMaximumGold(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        cands = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] and self.getNeigbors(grid, i, j) <= 2:
                    cands.append([i, j])
        res = [0]
        for i, j in cands:
            visited = [[0]*n for _ in range(m)]
            visited[i][j] = True
            self.dfs(grid, i, j, visited, grid[i][j], res)
        return res[0]

    def dfs(self, grid, i, j, visited, curr, res):
        m, n = len(grid), len(grid[0])
        res[0] = max(res[0], curr)
        for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            if 0 <= x < m and 0 <= y < n and grid[x][y] and not visited[x][y]:
                visited[x][y] = True
                self.dfs(grid, x, y, visited, curr+grid[x][y], res)
                visited[x][y] = False

    def getNeigbors(self, grid, i, j):
        res, m, n = 0, len(grid), len(grid[0])
        for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                res += 1
        return res

    def test(self):
        testCases = [
            [
                [1,0,7,0, 0,0],
                [2,0,6,0, 1,0],
                [3,5,6,7, 4,2],
                [4,3,1,0, 2,0],
                [3,0,5,0,20,0],
            ],
        ]
        for grid in testCases:
            res = self.getMaximumGold(grid)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
