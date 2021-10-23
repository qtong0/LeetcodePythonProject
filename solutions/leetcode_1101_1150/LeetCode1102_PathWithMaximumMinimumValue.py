from typing import List
import heapq


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [[-grid[0][0], 0, 0]]
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        while heap:
            val, i, j = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return -val
            for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    tmp = min(-val, grid[x][y])
                    heapq.heappush(heap, [-tmp, x, y])
                    visited[x][y] = True


    def test(self):
        test_cases = [
            [[5,4,5],[1,2,6],[7,4,6]],
            [[2,2,1,2,2,2],[1,2,2,2,1,2]],
            [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]],
        ]
        for grid in test_cases:
            res = self.maximumMinimumPath(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
