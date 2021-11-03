from typing import List


class Solution:
    # dp[c][k] is the prob of tossing c first coins and get k faced up.
    # dp[c][k] = dp[c - 1][k] * (1 - p) + dp[c - 1][k - 1] * p)
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0]*(target + 1)
        dp[0] = 1
        n = len(prob)
        for i in range(n):
            for k in range(min(i+1, target), -1, -1):
                dp[k] = (dp[k-1] if k > 0 else 0) * prob[i] + dp[k] * (1-prob[i])
        return dp[target]


    # Own DFS, TLE
    def probabilityOfHeads_own_dfs_TLE(self, prob: List[float], target: int) -> float:
        self.res = 0
        self.dfs(prob, 0, target, 1)
        return self.res

    def dfs(self, prob, i, target, curr):
        if i == len(prob):
            if target == 0:
                self.res += curr
            return
        if target > 0:
            self.dfs(prob, i+1, target-1, curr * prob[i])
        self.dfs(prob, i+1, target, curr * (1-prob[i]))

    def test(self):
        test_cases = [
            [[0.4], 1],
            [[0.5,0.5,0.5,0.5,0.5], 0],
        ]
        for prob, target in test_cases:
            res = self.probabilityOfHeads(prob, target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
