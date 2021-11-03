import collections
from typing import List


class Solution(object):
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)





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
