class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        if len(grid) < 1 or len(grid[0]) < 1:
            return -1
        m = len(grid)
        n = len(grid[0])
        if k > m-1+n-1:
            return m-1+n-1
        queue = [(0, 0, k, 0)]
        visited = set([(0, 0, k)])
        while queue:
            i, j, l, length = queue.pop(0)
            if i == m-1 and j == n-1:
                return length
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0:
                        if (x, y, l) not in visited:
                            queue.append((x, y, l, length+1))
                            visited.add((x, y, l))
                    else:
                        if l-1 >= 0 and (x, y, l-1) not in visited:
                            queue.append((x, y, l-1, length+1))
                            visited.add((x, y, l-1))
        return -1

    def test(self):
        test_cases = [
            [[[0,0,0],
              [1,1,0],
              [0,0,0],
              [0,1,1],
              [0,0,0]],1],
            [[[0,1,1],
              [1,1,1],
              [1,0,0]],1],
            [[[0,0],
              [1,0],
              [1,0],
              [1,0],
              [1,0],
              [1,0],
              [0,0],
              [0,1],
              [0,1],
              [0,1],
              [0,0],
              [1,0],
              [1,0],
              [0,0]
              ],4]
        ]
        for grid, k in test_cases:
            res = self.shortestPath(grid, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
