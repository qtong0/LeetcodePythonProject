from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        roots = list(range(n))
        for t, p1, p2 in logs:
            r1, r2 = self.find(roots, p1), self.find(roots, p2)
            if r1 != r2:
                roots[r1] = r2
                n -= 1
            if n <= 1:
                return t
        return -1

    def find(self, roots, p):
        while p != roots[p]:
            p = roots[p]
        return p

    def test(self):
        test_cases = [
            [
                [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]],
                4,
            ],
            [
                [
                    [20190101,0,1],
                    [20190104,3,4],
                    [20190107,2,3],
                    [20190211,1,5],
                    [20190224,2,4],
                    [20190301,0,3],
                    [20190312,1,2],
                    [20190322,4,5],
                ],
                6,
            ],
            [
                [
                    [0,2,0],
                    [1,0,1],
                    [3,0,3],
                    [4,1,2],
                    [7,3,1],
                ],
                4,
            ],
        ]
        for logs, n in test_cases:
            res = self.earliestAcq(logs, n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
