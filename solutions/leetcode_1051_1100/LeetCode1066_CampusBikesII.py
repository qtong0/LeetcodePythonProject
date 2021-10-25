from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(workers), len(bikes)
        dp = [[float('inf')]*(1 << n) for _ in range(m+1)]
        res = float('inf')
        dp[0][0] = 0
        for i in range(1, m+1):
            for s in range(1, 1 << n):
                for j in range(n):
                    if s & (1 << j) == 0:
                        continue
                    prev = s ^ (1 << j)
                    dp[i][s] = min(
                        dp[i][s],
                        dp[i-1][prev] + abs(workers[i-1][0] - bikes[j][0]) + abs(workers[i-1][1] - bikes[j][1])
                    )
                    if i == m:
                        res = min(res, dp[i][s])
        return res


    # DFS + Memorization, easier to understand
    # still TLE, but should be fine
    # TC *should be* O(n*m!)
    #
    def assignBikes_DFS_Mem(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        dp = [[0]*(1 << len(bikes)) for _ in range(len(workers))]
        return self.dfs(0, 0, workers, bikes, dp)

    def dfs(self, widx, takenBits, workers, bikes, dp):
        if widx == len(workers):
            return 0
        elif dp[widx][takenBits]:
            return dp[widx][takenBits]
        res = float('inf')
        for i in range(len(bikes)):
            if takenBits & 1 << i != 0:
                continue
            d = abs(workers[widx][0] - bikes[i][0]) + abs(workers[widx][1] - bikes[i][1])
            res = min(res, d + self.dfs(widx+1, takenBits | 1 << i, workers, bikes, dp))
        return res


    # DFS, TLE
    def assignBikes_DFS_TLE(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.res = float('inf')
        self.dfs2(workers, 0, bikes, 0)
        return self.res

    def dfs2(self, workers, i, bikes, sum_val):
        if i == len(workers):
            self.res = min(self.res, sum_val)
            return
        if not bikes:
            return
        for j in range(len(bikes)):
            bi, bj = bikes[j]
            wi, wj = workers[i]
            d = self.dist(bi, bj, wi, wj)
            self.dfs2(workers, i+1, bikes[:j] + bikes[j+1:], sum_val + d)

    def dist(self, i, j, x, y):
        return abs(i - x) + abs(j - y)

    def test(self):
        test_cases = [
            [[[0,0],[2,1]], [[1,2],[3,3]]],
            [[[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]],
            [[[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]],
        ]
        for workers, bikes in test_cases:
            res = self.assignBikes(workers, bikes)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
