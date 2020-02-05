class Solution:
    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        found, fresh = self.nextRound(grid)
        while found:
            found, fresh = self.nextRound(grid)
            res += 1
        return res if not fresh else -1

    def nextRound(self, grid):
        found = False
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 2:
                            grid[i][j] = -1
                            found = True
                            break
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    grid[i][j] = 2
                elif grid[i][j] == 1:
                    fresh += 1
        return found, fresh

    def test(self):
        testCases = [
            [[2,1,1],[1,1,0],[0,1,1]],
            [[2,1,1],[0,1,1],[1,0,1]],
            [[0,2]],
        ]
        for grid in testCases:
            res = self.orangesRotting(grid)
            print('res: %s' % res)


if __name__ == '__main__':
    Solution().test()
