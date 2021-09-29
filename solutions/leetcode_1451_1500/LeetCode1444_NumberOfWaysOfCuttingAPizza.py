from typing import List


class Solution:
    # Time O(k*m*n*(m+n))
    # Space O(k*m*n)
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        MOD = 10 ** 9 + 7
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c+1] + preSum[r+1][c] - preSum[r+1][c+1] + (pizza[r][c] == 'A')
        dp = [[[0] * n for _ in range(m)] for _ in range(k)]

        def dfs(k, r, c):
            if preSum[r][c] == 0:
                return 0
            if k == 0:
                return 1
            if dp[k][r][c] != 0:
                return dp[k][r][c]
            res = 0
            for nr in range(r + 1, m):
                if preSum[r][c] - preSum[nr][c] > 0:
                    res = (res + dfs(k - 1, nr, c)) % MOD
            for nc in range(c + 1, n):
                if preSum[r][c] - preSum[r][nc] > 0:
                    res = (res + dfs(k - 1, r, nc)) % MOD
            dp[k][r][c] = res
            return res

        return dfs(k - 1, 0, 0)

    def test(self):
        test_cases = [
            [["A..", "AAA", "..."], 3],
            [["A..", "AA.", "..."], 3],
            [["A..", "A..", "..."], 1],
        ]
        for pizza, k in test_cases:
            res = self.ways(pizza, k)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
