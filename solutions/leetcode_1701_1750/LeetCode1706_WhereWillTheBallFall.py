class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        res = list(range(n))
        for i in range(m):
            found = False
            for j in range(n):
                if res[j] != -1:
                    idx = res[j]
                    if grid[i][idx] == 1:
                        if idx == n-1 or grid[i][idx+1] == -1:
                            res[j] = -1
                        else:
                            res[j] = idx + 1
                            found = True
                    else:
                        if idx == 0 or grid[i][idx-1] == 1:
                            res[j] = -1
                        else:
                            res[j] = idx - 1
                            found = True
            if not found:
                break
        return res

    def test(self):
        test_cases = [
            [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]],
            [[-1]],
            [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]],
        ]
        for grid in test_cases:
            res = self.findBall(grid)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
