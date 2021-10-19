from typing import List


class Solution:
    # TC: O(m*n)
    # SC: O(m*n)
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance = [[float('inf')] * n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    distance[i][j] = 0
        res = -1
        while queue:
            i, j, d = queue.pop(0)
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and distance[x][y] > d+1:
                    distance[x][y] = d+1
                    queue.append((x, y, d+1))
                    res = max(res, d+1)
        return res

    def test(self):
        test_cases = [
            [[1,0,1],[0,0,0],[1,0,1]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        ]
        for grid in test_cases:
            res = self.maxDistance(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
