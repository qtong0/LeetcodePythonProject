from typing import List


class Solution:
    # DP
    def countPyramids(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reversed_grid = []
        for i in range(m-1, -1, -1):
            reversed_grid.append(grid[i][:])
        res = self.helper(grid)
        res += self.helper(reversed_grid)
        return res

    def helper(self, grid):
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            for j in range(1, n-1):
                if grid[i][j] and grid[i-1][j]:
                    grid[i][j] = min(grid[i-1][j-1], grid[i-1][j+1]) + 1
                    res += grid[i][j] - 1
        return res



    def test(self):
        test_cases = [
            [[0,1,1,0],[1,1,1,1]],
            [[1,1,1],[1,1,1]],
            [[1,0,1],[0,0,0],[1,0,1]],
            [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]],
        ]
        for grid in test_cases:
            res = self.countPyramids(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
