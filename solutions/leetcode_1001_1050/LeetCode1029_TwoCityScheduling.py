from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        res = 0
        n = len(costs) // 2
        print('n: %s' % n)
        for i in range(n):
            res += costs[i][0] + costs[i+n][1]
        return res


    # DFS, O(2^N), TLE (of course)
    def twoCitySchedCost_own_TLE(self, costs: List[List[int]]) -> int:
        m = len(costs)
        return self.helper(costs, 0, m//2, m//2, 0)

    def helper(self, costs, i, n1, n2, curr):
        if n1 == 0 and n2 == 0:
            return curr
        if n1 < 0 or n2 < 0:
            return float('inf')
        return min(
            self.helper(costs, i+1, n1-1, n2, curr+costs[i][0]),
            self.helper(costs, i+1, n1, n2-1, curr+costs[i][1])
        )

    def test(self):
        test_cases = [
            [[10,20],[30,200],[400,50],[30,20]],
            [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]],
            [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]],
        ]
        for costs in test_cases:
            res = self.twoCitySchedCost(costs)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
