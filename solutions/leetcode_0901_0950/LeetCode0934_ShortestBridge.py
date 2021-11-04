from typing import List


class Solution(object):
    def shortestBridge(self, A: List[List[int]]) -> int:
        queue = []
        i, j = self.findFirst(A)
        self.dfs(A, i, j, queue)

        n = len(A)
        step = 0
        while queue:
            queue1 = []
            for i, j in queue:
                for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            queue1.append((x, y))
            queue = queue1
            step += 1

    def findFirst(self, grid):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    return i, j

    def dfs(self, grid, i, j, queue):
        n = len(grid)
        grid[i][j] = -1
        queue.append((i, j))
        for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                self.dfs(grid, x, y, queue)


    ########## Own TLE Solution :S ##########
    def shortestBridge_own_TLE(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        found = False
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if not found:
                        found = True
                        self.bfs(A, i, j)
                    else:
                        res = min(res, self.find(A, i, j))
        return res

    def bfs(self, matrix, i, j):
        m, n = len(matrix), len(matrix[0])
        queue = [(i, j)]
        while queue:
            i0, j0 = queue.pop(0)
            matrix[i0][j0] = 2
            for i1, j1 in (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1):
                if 0 <= i1 < m and 0 <= j1 < n and matrix[i1][j1] == 1:
                    queue.append((i1, j1))

    def find(self, matrix, i, j):
        m, n = len(matrix), len(matrix[0])
        res = float('inf')
        queue = [(i, j, 0)]
        visited = set([(i, j)])
        while queue:
            i0, j0, d = queue.pop(0)
            if matrix[i0][j0] == 2:
                res = min(res, d-1)
            for i1, j1 in (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1):
                if 0 <= i1 < m and 0 <= j1 < n and matrix[i1][j1] != 1 \
                        and (i1, j1) not in visited:
                    visited.add((i1, j1))
                    queue.append((i1, j1, d+1))
        return res



    def test(self):
        testCases = [
            [[0,1],[1,0]],
            [[0,1,0],[0,0,0],[0,0,1]],
            [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]],
        ]
        for matrix in testCases:
            res = self.shortestBridge(matrix)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
