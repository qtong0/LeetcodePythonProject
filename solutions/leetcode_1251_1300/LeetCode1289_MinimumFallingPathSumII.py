from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1:
            return min(grid[0])
        for i in range(1, m):
            left, right = self.getLeftRight(grid[i-1])
            for j in range(n):
                if j == 0:
                    grid[i][j] += right[j+1]
                elif j == n-1:
                    grid[i][j] += left[j-1]
                else:
                    grid[i][j] += min(left[j-1], right[j+1])
        return min(grid[-1])

    def getLeftRight(self, row):
        n = len(row)
        left = [0]*n
        left[0] = row[0]
        right = [0]*n
        right[-1] = row[-1]
        for i in range(1, n):
            left[i] = min(left[i-1], row[i])
        for i in range(n-2, -1, -1):
            right[i] = min(right[i+1], row[i])
        return left, right


    def test(self):
        test_cases = [
            [[1,2,3],[4,5,6],[7,8,9]],
            [[7]],
        ]
        for grid in test_cases:
            res = self.minFallingPathSum(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
