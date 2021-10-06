from typing import List


class Solution:
    # Go from water to land and increase
    # You don't need to worry about height with difference greater than 1 on some neighbors
    # because it will never be possible
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        dp = [[-1]*n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dp[i][j] = 0
                    queue.append([i, j, 0])
        while queue:
            i, j, c = queue.pop(0)
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and dp[x][y] == -1:
                    dp[x][y] = c+1
                    queue.append([x, y, c+1])
        return dp

    def test(self):
        test_cases = [
            [[0,0],[1,1],[1,0]],
            [[0,1],[0,0]],
            [[0,0,1],[1,0,0],[0,0,0]],
        ]
        for isWater in test_cases:
            res = self.highestPeak(isWater)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
