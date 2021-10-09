from typing import List


class Solution:
    # DFS + Memorization!
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        presum = list(piles)
        for i in range(n-2, -1, -1):
            presum[i] += presum[i+1]
        memo = [[0]*n for _ in range(n)]
        return self.dfs(presum, 1, 0, memo)

    def dfs(self, presum, m, p, memo):
        if p + 2*m >= len(presum):
            return presum[p]
        if memo[p][m]:
            return memo[p][m]
        res, take = 0, 0
        for i in range(1, 2*m+1):
            # current take
            take = presum[p] - presum[p+i]
            # take max of current + what's left from other player max take
            res = max(res, take + presum[p+i] - self.dfs(presum, max(i, m), p+i, memo))
        memo[p][m] = res
        return res

    def test(self):
        test_cases = [
            [2,7,9,4,4],
            [1,2,3,4,5,100],
        ]
        for piles in test_cases:
            res = self.stoneGameII(piles)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
