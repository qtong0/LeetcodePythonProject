from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for start, end in intervals:
            if toBeRemoved[1] <= start:
                res.append([start, end])
            elif toBeRemoved[0] <= start < toBeRemoved[1] < end:
                res.append([toBeRemoved[1], end])
            elif toBeRemoved[0] <= start < end <= toBeRemoved[1]:
                continue
            elif start < toBeRemoved[0] < toBeRemoved[1] < end:
                res.append([start, toBeRemoved[0]])
                res.append([toBeRemoved[1], end])
            elif start < toBeRemoved[0] <= end < toBeRemoved[1]:
                res.append([start, toBeRemoved[0]])
            else:
                res.append([start, end])
        return res


    def test(self):
        test_cases = [
            [
                [[0, 100]],
                [0, 50],
            ],
            [
                [[0,2],[3,4],[5,7]],
                [1,6],
            ],
            [
                [[0,5]],
                [2,3],
            ],
            [
                [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]],
                [-1,4],
            ],
        ]
        for intervals, toBeRemoved in test_cases:
            res = self.removeInterval(intervals, toBeRemoved)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
