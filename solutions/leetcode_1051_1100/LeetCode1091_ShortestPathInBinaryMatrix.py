class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if not grid or not grid[0] or grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        query = [(0, 0, 1)]
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        while query:
            i, j, d = query.pop(0)
            if i == n-1 and j == n-1:
                return d
            for x, y in (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), \
                (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1):
                if 0 <= x < n and 0 <= y < n and not visited[x][y] and not grid[x][y]:
                    visited[x][y] = True
                    query.append((x, y, d+1))
        return -1
