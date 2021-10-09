class Solution(object):
    # TC: O(m×n+L) where L is the number of operations
    # m is the number of rows and n is the number of columns
    #
    def numIslands2(self, m, n, positions):
        res = []
        # Use list(range(m*n)) instead of [-1]*(m*n)
        # In this case, it works, but list(range(n)) handles duplicate (a==a) scenario better
        roots = list(range(m*n))
        grid = [[False]*n for _ in range(m)]
        count = 0
        for pos in positions:
            i, j = pos[0], pos[1]
            if grid[i][j]:
                res.append(res[-1])
                continue
            grid[i][j] = True
            count += 1
            root0 = i*n+j
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    root = self.getRoot(roots, x*n+y)
                    if root != root0:
                        count -= 1
                        roots[root] = root0
            res.append(count)
        return res

    def getRoot(self, roots, ind):
        while roots[ind] != ind:
            ind = roots[ind]
        return ind

    def test(self):
        testCases = [
            (3, 3, [[0,0], [0,1], [1,2], [2,1]]),
            [
                3,
                3,
                [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]],
            ],
            [
                8,
                4,
                [[0,0],[7,1],[6,1],[3,3],[4,1]],
            ],
        ]
        for m, n, positions in testCases:
            print('m: %s' % (m))
            print('n: %s' % (n))
            print('positions: %s' % (positions))
            result = self.numIslands2(m, n, positions)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
