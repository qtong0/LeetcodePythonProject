from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        # costs[i][j] is the total travel distance from houses[i:j] to a mailbox when putting within houses[i:j]
        # the best way to put the mailbox is at median position
        costs = [[0]*(1+n) for _ in range(1+n)]
        mem = [[0]*(1+n) for _ in range(1+n)]
        houses.sort()
        for i in range(n):
            for j in range(n):
                median_pos = houses[(i+j)//2]
                for l in range(i, j+1):
                    costs[i][j] += abs(median_pos - houses[l])
        return self.dfs(houses, costs, mem, n, k, 0)

    def dfs(self, houses, costs, mem, n, k, i):
        if k == 0 and i == n:
            return 0
        if k == 0 or i == n:
            return float('inf')
        if mem[k][i]:
            return mem[k][i]
        res = float('inf')
        for j in range(i, n):
            res = min(res, costs[i][j] + self.dfs(houses, costs, mem, n, k-1, j+1))
        mem[k][i] = res
        return res

    def test(self):
        test_cases = [
            [[1,4,8,10,20], 3],
            [[2,3,5,12,18], 2],
            [[7,4,6,1], 1],
            [[3,6,14,10], 4],
        ]
        for houses, k in test_cases:
            res = self.minDistance(houses, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
