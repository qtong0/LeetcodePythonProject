from functools import lru_cache
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        min_costs2 = [min(cost[i][j] for i in range(m)) for j in range(n)]

        @lru_cache(None)
        def dfs(i, mask):
            res = 0 if i >= m else float('inf')
            if i >= m:
                for j in range(n):
                    if mask & (1 << j) == 0:
                        res += min_costs2[j]
            else:
                for j in range(n):
                    res = min(res, cost[i][j] + dfs(i+1, mask | (1 << j)))
            return res

        return dfs(0, 0)



    def test(self):
        test_cases = [
            [[15, 96], [36, 2]],
            [[1, 3, 5], [4, 1, 1], [1, 5, 3]],
            [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]],
        ]
        for cost in test_cases:
            res = self.connectTwoGroups(cost)
            print('res: %s' % res)
            print('-='*30 + '-')



if __name__ == '__main__':
    Solution().test()
