from typing import List


class Solution(object):
    # TC: O(N^3)
    # SC: O(N*3)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[[float('-inf')]*n for _ in range(n)] for _ in range(m)]
        return max(0, self.dfs(m-1, n-1, n-1, grid, memo))

    def dfs(self, x1, y1, y2, grid, memo):
        x2 = x1 + y1 - y2
        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            return -1
        if grid[x1][y1] < 0 or grid[x2][y2] < 0:
            return -1
        if x1 == 0 and y1 == 0:
            return grid[x1][y1]
        if memo[x1][y1][y2] != float('-inf'):
            return memo[x1][y1][y2]
        memo[x1][y1][y2] = max(
            self.dfs(x1, y1-1, y2-1, grid, memo),
            self.dfs(x1-1, y1, y2, grid, memo),
            self.dfs(x1-1, y1, y2-1, grid, memo),
            self.dfs(x1, y1-1, y2, grid, memo),
        )
        if memo[x1][y1][y2] >= 0:
            memo[x1][y1][y2] += grid[x1][y1]
            if y1 != y2:
                memo[x1][y1][y2] += grid[x2][y2]
        return memo[x1][y1][y2]


    def cherryPickup_DP_only(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = (N<<1)-1
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for n in range(1, M):
            for i in range(N-1, -1, -1):
                for p in range(N-1, -1, -1):
                    j = n-i
                    q = n-p
                    if j<0 or j>=N or q<0 or q>=N or grid[i][j]<0 or grid[p][q]<0:
                        dp[i][p] = -1
                        continue
                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p-1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p-1])
                    if dp[i][p] >= 0:
                        dp[i][p] += grid[i][j]+(grid[p][q] if i!=p else 0)
        return max(dp[-1][-1], 0)
    
    def test(self):
        testCases = [
            [
                [0, 1, -1],
                [1, 0, -1],
                [1, 1,  1]
            ],
        ]
        for grid in testCases:
            res1 = self.cherryPickup(grid)
            res2 = self.cherryPickup_DP_only(grid)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
