from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees = {}
        for i, m in enumerate(manager):
            if i != headID:
                employees[m] = employees.get(m, []) + [i]
        queue = [[headID, informTime[headID]]]
        res = 0
        while queue:
            node, time = queue.pop(0)
            for empl in employees.get(node, []):
                empl_time = time+informTime[empl]
                res = max(res, empl_time)
                queue.append([empl, empl_time])
        return res

    def test(self):
        test_cases = [
            [1, 0, [-1], [0]],
            [6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]],
            [7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]],
            [4, 2, [3,3,-1,2], [0,0,162,914]],
            [15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]],
            [11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]],
        ]
        for n, headID, manager, informTime in test_cases:
            res = self.numOfMinutes(n, headID, manager, informTime)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
