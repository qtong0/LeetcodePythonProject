from typing import List


class Solution(object):
    # 1) For each hit (i, j), if grid[i][j]==0, set grid[i][j]=-1 otherwise set grid[i][j]=0.
    #       Since a hit may happen at an empty position, we need to separate emptys from bricks.
    #
    # 2) For i in [0, n], do dfs at grid[i][0] and mark no-dropping bricks. Here we get the grid after all hits.
    #
    # 3) Then for each hit (i,j) (reversely), first we check grid[i][j]==-1,
    #       if yes, it's empty, skip this hit.
    #       Then we check whether it's connected to any no-dropping bricks or it's at the top,
    #       if not, it can't add any no-dropping bricks, skip this hit.
    #       Otherwise we do dfs at grid[i][j], mark new added no-dropping bricks and record amount of them.
    #
    # 4) Return the amounts of new added no-dropping bricks at each hits.
    #
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n) or grid[i][j]!=1:
                return 0
            res = 1
            grid[i][j] = 2
            res += sum(dfs(x, y) for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)])
            return res
        
        # Check whether (i, j) is connected to Not Failling Bricks
        def is_connected(i, j):
            return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2\
                                for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]])
        
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1
        
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        # Reversely and the block of each hits and get count of newly add bricks
        res = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                res[k] = dfs(i, j)-1
        return res
    
    def test(self):
        testCases = [
            [
                [
                    [1,0,0,0],
                    [1,1,1,0]
                ],
                [[1,0]],
            ],
            [
                [
                    [1,0,0,0],
                    [1,1,0,0]
                ],
                [[1,1],[1,0]],
            ],
        ]
        for grid, hits in testCases:
            print('grid: %s' % grid)
            print('hits: %s' % hits)
            result = self.hitBricks(grid, hits)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
