from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        queue = [[0, 0]]
        while queue:
            i, j = queue.pop(0)
            if i == m-1 and j == n-1:
                return True
            for x, y in self.getNext(grid, i, j):
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and self.isValid(grid, i, j, x, y):
                    queue.append([x, y])
                    visited[x][y] = True
        return False

    def isValid(self, grid, i, j, x, y):
        if x == i:
            if y == j+1:
                return grid[x][y] in (1, 3, 5)
            elif y == j-1:
                return grid[x][y] in (1, 4, 6)
        elif x == i-1:
            return grid[x][y] in (2, 3, 4)
        elif x == i+1:
            return grid[x][y] in (2, 5, 6)
        return False

    def getNext(self, grid, i, j):
        if grid[i][j] == 1:
            return [[i, j-1], [i, j+1]]
        elif grid[i][j] == 2:
            return [[i-1, j], [i+1, j]]
        elif grid[i][j] == 3:
            return [[i, j-1], [i+1, j]]
        elif grid[i][j] == 4:
            return [[i, j+1], [i+1, j]]
        elif grid[i][j] == 5:
            return [[i-1, j], [i, j-1]]
        else:
            return [[i-1, j], [i, j+1]]



    def test(self):
        test_cases = [
            [[2,4,3],[6,5,2]],
            [[1,2,1],[1,2,1]],
            [[1,1,2]],
            [[1,1,1,1,1,1,3]],
            [[2],[2],[2],[2],[2],[2],[6]]
        ]
        for grid in test_cases:
            res = self.hasValidPath(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
